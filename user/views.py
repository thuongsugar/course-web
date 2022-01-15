from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.views.generic import FormView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse




from .form import RegisterUserForm
from .models import User
# Create your views here.
class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get(self, request, *args: str, **kwargs):
        if request.user.is_authenticated :
            return redirect('/')
        return super().get(request, *args, **kwargs)
    
        

class UserRegisterView(FormView):
    template_name = 'user/register.html'
    form_class = RegisterUserForm

    def form_valid(self, form):
        user_data = form.cleaned_data
        User.objects.create_user(username=user_data['username'],
                                email=user_data['email'],
                                password=user_data['password1']
        )
        return redirect('course:login')

class UserLogoutView(LogoutView):
    next_page = 'course:login'

# class UserChangePass(LoginRequiredMixin,View):
#     login_url = 'course:login'
#     def post(self,request):
#         user = User.objects.get(pk=request.user.id)
#         user.set_password()
#     def get(self,request):
#         return HttpResponse('data')

class UserChangePass(PasswordChangeView):
    success_url = ''
    template_name = 'user/change_pass.html'
    title = ('Thay đổi mật khẩu')
    def get_context_data(self, **kwargs):
        print(super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)