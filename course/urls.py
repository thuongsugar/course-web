from django.urls import path,include,re_path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import CourseView, IndexView,CategoryDetailView,CourseAPI,CourseIntroduceView, LearningView
from user.views import UserLoginView,UserRegisterView,UserLogoutView,UserChangePass
app_name = 'course'
urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('category/<int:pk>/course/', CategoryDetailView.as_view(),name='category_detail'),
    path('course/', CourseView.as_view(),name='courses'),
    path('course/<int:pk>', CourseIntroduceView.as_view(),name='course_register'),
    path('learning/<int:pk>', LearningView.as_view(),name='learning'),

    #tim kiem
    path('api/course/', CourseAPI.as_view(),name='course_api'),

    # path('course/<int:pk>/lesson', CourseView.as_view(),name='courses'),
    


    path('login', UserLoginView.as_view(),name='login'),
    path('register', UserRegisterView.as_view(),name='register'),
    path('logout', UserLogoutView.as_view(),name='logout'),
    path('change-password', UserChangePass.as_view(),name='change_pass'),

    path('password_reset/',
        PasswordResetView.as_view(
            template_name='user/reset_password.html',
            # success_url = reverse_lazy('course:password_reset_done')
            success_url=reverse_lazy('course:password_reset_done'),
            email_template_name = 'user/password_reset_email.html',
            subject_template_name = 'user/password_reset_subject.txt'

    ),
        name="password_reset"),

    path('password_reset/done',
        PasswordResetDoneView.as_view(
            template_name='user/reset_password_done.html'
    ),
        name="password_reset_done"),
    
    path('password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='user/reset_password_confirm.html',
            success_url=reverse_lazy('course:password_reset_complete')
    ),
        name="password_reset_confirm"),

     path('password_reset/completed/',
        PasswordResetCompleteView.as_view(
            template_name='user/reset_password_completed.html'
    ),
        name="password_reset_complete"),


    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
