from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Шаблоны для доступа к обработчикам смены пароля.
    path(
        'password_change/', 
        auth_views.PasswordChangeView.as_view(), name='password_change'
        ),
    path(
        'password_change/done/', 
        auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'
        ),
    # Обработчики действий со статьями.
    #path('login/', views.user_login, name='login'),
    # авторизация пользователей посредством системы аутентификации Django.
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # рабочий стол
    path('', views.dashboard, name='dashboard'),
]