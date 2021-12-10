from django.urls import path
from medicSearch.views.AuthView import LoginForm, login_view, register_view

urlpatterns = [
    path("login", login_view, name='login'),
    path('register', register_view, name='register')
]