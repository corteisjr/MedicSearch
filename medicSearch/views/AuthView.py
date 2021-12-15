from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from medicSearch.models.Profile import Profile
from medicSearch.forms.AuthForm import LoginForm, RegisterForm, RecoveryForm

def login_view(request):
    loginForm = LoginForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)
        
        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect('/')
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorrectos'
                }
                
    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registrar',
        'link_href': '/register'
    }
    
    return render(request, template_name='auth/auth.html', context=context, status=200)

def register_view(request):
    registerForm = RegisterForm()
    message = None
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)
        
        if registerForm.is_valid():
            #verifcando se o usuário existe
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()
            
            if verifyUsername is not None:
                message = {
                    'type': 'danger',
                    'text': 'Já existe um usuário com este username!'
                }
            elif verifyEmail is not None:
                message = {
                    'type': 'danger',
                    'text': 'Já existe um usúario com esse e-mail!'
                }
            else:
                user = User.objects.create_user(username, email, password)
                if user is not None:
                    message = {
                        'type': 'success',
                        'text': 'Conta criada com sucesso'
                    }
                else:
                    message = {
                        'type': 'danger',
                        'text': 'Um erro ocorreu ao tentar criar a conta.'
                    }
                    
    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login'
        
    }
                    
    return render(request, template_name='auth/auth.html', context=context, status=200)

def logout_view(request):
    logout(request)
    return redirect('/login')
         
#recoperar senha
def recovery_view(request):
    recoveryForm = RecoveryForm()
    message = None
    
    if request.method == 'POST':
        recoveryForm = RecoveryForm(request.POST)
        
        if recoveryForm.is_valid():
            email = request.POST['email']
            profile = Profile.objects.filter(user__email=email).first()
            if profile is not None:
                try:
                    send_email(profile)
                    message = {
                        'type': 'success',
                        'text': 'Um e-mail foi enviado para sua caixa de entrada'
                    }
                
                except:
                    message = {
                        'type': 'danger',
                        'text': 'Erro no envio do e-mail.'
                    }
            else:
                message = {
                    'type': 'danger',
                    'text': 'E-mail inexistente'
                }
        else:
            
            message = {'type': 'danger', 'text': 'Formulário inválido'}
            
    context = {
        'form': recoveryForm,
        'message': message,
        'title': 'Recuperar Senha',
        'button_text': 'Recuperar',
        'link_text': 'Login',
        'link_href': '/login'
    }
    
    return render(request, template_name='auth/auth.html', context=context, status=200)


def send_email(profile):
    pass