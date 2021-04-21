

from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views,views

urlpatterns = [
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', views.signup, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]

