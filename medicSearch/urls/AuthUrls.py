from django.urls import path
from medicSearch.views.AuthView import LoginForm, login_view

urlpatterns = [
    path("login", login_view, name='login')
]