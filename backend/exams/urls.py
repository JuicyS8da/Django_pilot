from django.urls import path
from .views import TestsListView, exam_detail, exam_finish

urlpatterns = [
    path('tests/', TestsListView.as_view(), name='tests'),
    path('exam/<int:exam_id>/', exam_detail, name='test_process'),
    path('exam/<int:exam_id>/finish/', exam_finish, name='exam_finish'),
]