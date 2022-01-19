from django.contrib import admin
from .models import Result

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id','score','cheat','create_date','user','quiz']
    list_filter = ['quiz']
    ordering = ('cheat','score')

# Register your models here.
admin.site.register(Result,ResultAdmin)
