from django.urls import path,include
from .views import QuizView,QuizStart,QuizSave,ResultStatistical
app_name = 'quiz'
urlpatterns = [
    path('quiz', QuizView.as_view(),name='index'),
    path('quiz/<int:pk>/',QuizStart.as_view(),name='quiz_detail'),
    path('quiz/<int:pk>/save',QuizSave.as_view(),name='quiz_save'),
    path('statistical',ResultStatistical.as_view(),name='statistical')
]
