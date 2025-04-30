from django.db import models
from django.contrib.auth import get_user_model

class Exam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    
    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Question {self.id} for {self.exam.title}"

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Option for Question {self.question.id}"

class UserAnswer(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.CASCADE)
    short_answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Answer by {self.user.username} for {self.question.text}"
    
    def return_right_answer(self):
        return self.question.options.filter(is_correct=True).first()

class ExamResult(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result of {self.user.username} for {self.exam.title}"
