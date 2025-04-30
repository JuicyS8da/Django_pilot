import nested_admin
from django.contrib import admin
from .models import Exam, Question, Option

class OptionInline(nested_admin.NestedTabularInline):
    model = Option
    extra = 1

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    extra = 1
    inlines = [OptionInline]

class ExamAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Exam, ExamAdmin)