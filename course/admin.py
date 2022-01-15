from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category,Course,Lesson

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'

class LessonInline(admin.StackedInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    forms = CourseForm
    inlines = [LessonInline]
# Register your models here.
admin.site.register(Category)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson)
