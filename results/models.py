from django.db import models
from user.models import User
from quiz.models import Quiz
# Create your models here.
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    cheat = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) :
        return str(self.score)