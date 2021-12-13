from django.urls import path, include
from medicSearch.views.AuthView import LoginForm, login_view, logout_view, register_view

urlpatterns = [
    path("login", login_view, name='login'),
    path('register', register_view, name='register'),
    path("logout", logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]