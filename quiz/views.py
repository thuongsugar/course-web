import json
from statistics import mode
from unittest import result
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from results.models import Result
from .models import Quiz,Question,Answers
from course.models import Course
# Create your views here.
class QuizView(LoginRequiredMixin,ListView):
    login_url = 'course:login'
    template_name = 'quiz/index.html'
    model = Quiz
    context_object_name = 'quiz_list'

    def get(self, request, *args, **kwargs):
        if request.GET.get('course_id') is not None:
            course_id = request.GET.get('course_id')
            print(course_id)
            course = Course.objects.get(pk = course_id)

            # neu chua dang ki khoa hoc
            if not course.user_register.filter(pk=request.user.id).exists():
               return redirect('course:course_register', pk=course_id)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        course_id = self.request.GET.get('course_id')
        if course_id is None:
            course_registed = Course.objects.filter(user_register=self.request.user.id)
            quiz = Quiz.objects.filter(course__id__in=course_registed)
            return quiz
        else:
            course = Course.objects.get(pk = course_id)
            # neu chua dang ki khoa hoc
            quiz = course.quiz_set.all()
            return quiz
    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        course_registed = Course.objects.filter(user_register=self.request.user.id)
        context['course_registed'] = course_registed
        if self.request.GET.get('course_id') is None:
            context['param'] = None    
        else:
            context['param'] = int(self.request.GET.get('course_id'))
        print(context)
        return context

class QuizStart(View):
    def get(self,request,pk):
        quiz = Quiz.objects.get(pk=pk) 
        question = []
        for q in quiz.get_question():
            answers = []
            for a in q.get_answer():
                answers.append(a.content)
            question.append({str(q.content):answers})
        return JsonResponse({
            'data':question,
            'time':quiz.time
        })

class QuizSave(View):
    def post(self,request,pk):
        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        questions = []
        score = 0
        answer_correct = None
        rusult = []
        data = json.loads(request.body) 
        cheat = data.pop('cheat')
        print(cheat)

        for k in data.keys():
            q = Question.objects.get(content=k)
            questions.append(q)
        for q in questions:
            answer_selected = data.get(q.content)
            all_answer = q.get_answer()
            for ans in all_answer:
                if answer_selected == ans.content:
                    if ans.correct :
                        score += 1
                        answer_correct = ans.content
                else:
                    if ans.correct:
                        answer_correct = ans.content
            rusult.append({str(q.content):{'answer_correct':answer_correct,'answered':answer_selected}})
        score_ = 10 / quiz.number_of_question * score
        Result.objects.create(user=user,quiz=quiz,score=score_,cheat=cheat)
        # return render(request=request,template_name='quiz/quiz_result.html',context={'score':score_,'result':rusult})
        return JsonResponse({'score':score_,'result':rusult})

class ResultStatistical(LoginRequiredMixin,ListView):
    login_url = 'course:login'
    template_name = 'quiz/show_result.html'
    model = Result
    context_object_name = 'result_list'
    def get_queryset(self):
        result = Result.objects.filter(user = self.request.user.id).order_by('-create_date')

        return result