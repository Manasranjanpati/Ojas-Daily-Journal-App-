

from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views,views

urlpatterns = [

    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_change_form/', auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change_form'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset_form'),
    path('password_done_view/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_confirm_view/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_complete_view/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
    path('signup/', views.signup, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]

