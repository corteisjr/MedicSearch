from django.urls import path
from medicSearch.views.ProfileView import edit_profile, list_profile_view

urlpatterns = [
    path('', list_profile_view),
    path("<int:id>", list_profile_view, name='profile'),
    path("edit", edit_profile, name='edit-profile'),
    
]
