from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category,Course,Lesson

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'

class LessonInline(admin.StackedInline):
    model = Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id','subject','link','created_date','course']
    list_filter = ['course']
    ordering = ('created_date',)


class CourseAdmin(admin.ModelAdmin):
    forms = CourseForm
    inlines = [LessonInline]
    list_display = ['id','subject','active','category','img']
    list_filter = ['category']
    readonly_fields = ['img']
    def img(self, course):
        return mark_safe(
            "<img src='/static/{img_url}' width='120px' alt='{alt}' />"
            .format(img_url=course.image, alt=course.subject)
        )

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['img']
    list_display = ['id','name','img']

    def img(self, category):
        return mark_safe(
            "<img src='/static/{img_url}' width='120px' alt='{alt}' />"
            .format(img_url=category.image, alt=category.name)
        )
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
