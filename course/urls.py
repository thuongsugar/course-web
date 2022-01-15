from django.urls import path,include,re_path
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


    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
