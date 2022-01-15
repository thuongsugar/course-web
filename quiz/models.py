from django.db import models
from course.models import Course
from user.models import User
# Create your models here.
class Quiz(models.Model):
    class Meta:
        unique_together = ('name', 'course')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    name = models.CharField(unique=True, max_length=100, null=False)
    number_of_question = models.IntegerField(null=True)
    time = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.course}"

    def get_question(self):
        return self.question_set.all()[:self.number_of_question]


class Question(models.Model):
    # class Meta:
    #     unique_together = ('content', 'quiz')
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.content}"
    
    def get_answer(self):
        return self.answers_set.all()

class Answers(models.Model):
    class Meta:
        unique_together = ('content', 'question')
    content = models.CharField(max_length=255, null=False)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"question: {self.question.content}, answers:{self.content}, correct:{self.correct}"




