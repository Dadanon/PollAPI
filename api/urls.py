from django.urls import path

from .views import questions_view, question_detail_view

urlpatterns = [
    path('questions/', questions_view),
    path('questions/<int:question_id>/', question_detail_view, name='question_detail'),
]