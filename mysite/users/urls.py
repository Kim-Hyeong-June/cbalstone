from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 코드 추가하기
    #회원가입 페이지
    path('signup/', views.signup, name='signup'),
    # 프로필 페이지
    path('<str:username>/', views.profile, name='profile'),
    # 프로필 수정 페이지
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    
    path('', views.main, name='main'),
]
