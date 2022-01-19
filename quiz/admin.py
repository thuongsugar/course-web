from django.contrib import admin
from .models import Quiz, Question,Answers
from django.utils.html import mark_safe

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id','name','number_of_question','question_all','time','course']
    list_filter = ['course']
    readonly_fields = ['question_all']
    def question_all(self, quiz):
        return mark_safe(
            quiz.question_set.all().count()
        )

class AnswerInline(admin.TabularInline):
    model = Answers
    extra = 4

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','content','correct','question']
    list_filter = ['question']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['id','content','quiz']
    list_filter = ['quiz']



# Register your models here.
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers,AnswerAdmin)