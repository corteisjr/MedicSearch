from django import forms
from django.forms.widgets import TextInput

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    
#cadastro de usuarios
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    
#recoperar senha
class RecoveryForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))    