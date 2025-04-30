from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Exam, Question, Option, UserAnswer, ExamResult
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.utils.timezone import localtime

class TestsListView(ListView):
    model = Exam
    template_name = 'test_start.html'
    context_object_name = 'tests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exams = Exam.objects.all()
        user = self.request.user

        # Собираем результаты для всех экзаменов
        exam_results = ExamResult.objects.filter(user=user, exam__in=exams)
        results_by_exam = {result.exam.id: result for result in exam_results}

        # Создаем список экзаменов с результатами
        exams_with_results = []
        for exam in exams:
            result = results_by_exam.get(exam.id)
            exams_with_results.append({
                'exam': exam,
                'last_score': result.score if result else None,
                'last_date': localtime(result.date_taken).strftime('%d.%m.%Y %H:%M') if result else None
            })

        context['exams_with_results'] = exams_with_results
        return context


@login_required
def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = list(exam.questions.all().order_by('id'))

    question_id = request.GET.get('question_id')
    current_question = get_object_or_404(Question, id=question_id) if question_id else questions[0]

    if request.method == 'POST':
        selected_option_id = request.POST.get(f'answer_{current_question.id}')
        
        if selected_option_id:
            selected_option = get_object_or_404(Option, id=selected_option_id)
            
            # Сохраняем или обновляем UserAnswer
            UserAnswer.objects.update_or_create(
                user=request.user,
                question=current_question,
                defaults={'selected_option': selected_option}
            )

        current_index = questions.index(current_question)
        if current_index + 1 < len(questions):
            next_question = questions[current_index + 1]
            return HttpResponseRedirect(
                f"{reverse('test_process', args=[exam.id])}?question_id={next_question.id}"
            )
        else:
            return redirect('exam_finish', exam_id=exam.id)

    user_answer = UserAnswer.objects.filter(user=request.user, question=current_question).first()

    return render(request, 'test_process.html', {
        'exam': exam,
        'current_question': current_question,
        'questions': questions,
        'user_answer': user_answer,
    })

@login_required
def exam_finish(request, exam_id):
    user = request.user
    exam = get_object_or_404(Exam, id=exam_id)

    questions = exam.questions.all()
    user_answers = UserAnswer.objects.filter(user=user, question__in=questions)

    total_questions = questions.count()
    correct_answers = 0

    result_details = []

    for user_answer in user_answers:
        # Получаем правильный ответ для текущего вопроса
        correct_option = user_answer.question.options.filter(is_correct=True).first()

        # Проверяем, совпадает ли выбранный ответ с правильным
        is_correct = user_answer.selected_option == correct_option

        if is_correct:
            correct_answers += 1

        result_details.append({
            'question': user_answer.question.text,
            'user_answer': user_answer.selected_option.text if user_answer.selected_option else "No answer selected",
            'correct_answer': correct_option.text if correct_option else "No correct answer",
            'is_correct': is_correct
        })

    score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    # Сохраняем результат
    ExamResult.objects.update_or_create(
        user=user,
        exam=exam,
        defaults={'score': round(score, 2)}
    )

    return render(request, 'test_review.html', {
        'exam': exam,
        'date_taken': ExamResult.objects.get(user=user, exam=exam).date_taken.strftime('%d.%m.%Y'),
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'score': round(score, 2),
        'result_details': result_details,
    })
