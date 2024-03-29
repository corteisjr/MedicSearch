from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from medicSearch.models import Profile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from medicSearch.forms.UserProfileForm import UserForm, UserProfileForm


def list_profile_view(request, id=None):
    profile = None
    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    elif id is not None:
        profile = Profile.objects.filter(user__id=id).first()
    elif not request.user.is_authenticated:
        return redirect(to=' /')
    
    favorites = profile.show_favorites()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)
     
    ratings = profile.show_ratings()
    if len(ratings) > 0:
        paginator = Paginator(ratings, 8)
        page = request.GET.get(' page')
        ratings = paginator.get_page(page)   
    
    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings
    }
    
    return render(request, template_name='profile/Profile.html', context=context, status=200)    
    
@login_required   
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    emailunused = True
    
    message = None
    
    if request.method == 'POST':
        profileForm = UserProfileForm(request.POST, request.FILES,  instance=profile)
        userForm = UserForm(request.POST, instance=request.user)
        
        # Verifica se o email que o usuario esta usando em seu perfil existe em outro perfil
        verifyEmail = Profile.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailunused = verifyEmail is None
    else:      
        profileForm = UserProfileForm(instance=profile)
        #cria instancia da classe UserForm
        userForm = UserForm(instance=request.user)
    
    if profileForm.is_valid() and userForm.is_valid() and emailunused:
        profileForm.save()
        userForm.save()  

        message = {'type': 'success', 'text': 'Dados actualizados'}
    else:
        if request.method == 'POST':
            if emailunused:
                # Se o e-mail não está em uso mas o formulário tiver algum dado inválido.
                message = {'type': 'danger', 'text': 'Dados inválidos'}
            else:
                    # Se o e-mail que o usuário tentou usar já está em uso por outra pessoa.
                message = {'type': 'warning', 'text': 'E-mail já usado por outro usuário'}
    context = {
        'profileForm': profileForm,
        'userForm':  userForm,
        'message': message
    }
    
    return render(request, template_name='user/profile.html', context=context, status=200)


        