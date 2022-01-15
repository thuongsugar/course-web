from django.core import serializers
from django.db.models import Count
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.base import View

from user.models import User
from .models import Category, Course,Lesson
# Create your views here.
class IndexView(ListView):
    model = Category
    template_name = 'course/index.html'
    context_object_name = 'category_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_user'] = User.objects.count()
        return context

class CategoryDetailView(ListView):
    model = Course
    template_name = 'course/courses_category_detail.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        try :
            return Course.objects.filter(category=self.kwargs.get('pk'))
        except Course.DoesNotExist :
            return []

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        course_list = context['course_list']
        if current_user.id == None:
            course_list = course_list.filter().values().annotate(total=Count('user_register')).order_by('-total')
            context['course_list'] = course_list
            return context

        course_registed = []
        
        #khoa da dang ki
        course_registed = course_list.filter(user_register = current_user.id)
        context['course_registed'] = course_registed

        #lay ra khoa chua dang ki
        course_list = course_list.filter().exclude(user_register= current_user.id)


        print(len(course_list))
        if len(course_list) == 0 :
            context['course_list'] = []
            return context

        #dem so nguoi dang ki 'total'
        course_list = course_list.filter().values().annotate(total=Count('user_register')).order_by('-total')
        context['course_list'] = course_list
        print(course_list)
        return context


class CourseView(ListView):
    model = Course
    template_name = 'course/course_registed.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        courses = context['courses']
        if current_user.id is None:
            courses = courses.filter().values().annotate(total=Count('user_register')).order_by('-total')
            context['courses'] = courses
            return context
        else:
            courses = courses.filter(user_register= current_user.id)
            context['courses'] = courses
        return context


#cho tim kiem
class CourseAPI(View):
    def get(self,request):
        course = Course.objects.filter(active=True)
        q = request.GET.get('q')
        print(q)
        category_id = request.GET.get('category_id')

        if q is not None:
            course = course.filter(subject__icontains=q)
        if category_id is not None :
            course = course.filter(category_id=category_id)
        print(course)
        data = serializers.serialize('json',course,fields=('subject','image'))
        return HttpResponse(data,content_type="application/json")

class CourseIntroduceView(UpdateView):
    model = Course
    fields = []

    template_name_suffix = '_register_form'
# course_register_form.html
    @method_decorator(login_required(login_url='course:login'))
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        course = self.get_object()
        course.user_register.add(self.request.user.id)
        course.save()
        #chuyen sang page learning
        return redirect('course:learning', pk=course.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_registed'] = context['object'].user_register.filter(pk=self.request.user.id).exists()
        print(context['is_registed'])
        print(context['course'].lesson_set.all())
        return context
class LearningView(ListView):
    template_name = 'course/learn.html'
    model = Lesson
    context_object_name = 'lessons'

    def get(self, request, *args, **kwargs):
        course = Course.objects.get(pk=self.kwargs.get('pk'))
        #check ng dung da dki chua
        if not course.user_register.filter(pk=request.user.id).exists():
           return redirect('course:course_register', pk=self.kwargs.get('pk'))
        print(course)
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        
        return Lesson.objects.filter(course=self.kwargs.get('pk'),active=True)
        