from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100,error_messages={'required':'This field is required.'})
    class Meta:
        model = User
        fields = ['username','email']
        field_classes = {'username': UsernameField}
        widgets = {
            'email' : forms.EmailInput(attrs={'required':True})
        }