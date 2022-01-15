from django.contrib import admin
from .models import Quiz, Question,Answers

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','name','number_of_question','time','course']
    list_filter = ['course']

class AnswerInline(admin.TabularInline):
    model = Answers
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


# Register your models here.
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers)