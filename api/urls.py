from django.urls import path

from . import views

urlpatterns = [
    path('questions/', views.questions_view),
    path('questions/<int:question_id>/', views.question_detail_view, name='question_detail'),
    path('questions/<int:question_id>/choices/', views.choices_view),
]