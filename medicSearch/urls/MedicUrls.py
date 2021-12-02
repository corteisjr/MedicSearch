from  django.urls import path
from medicSearch.views.MedicView import add_favorite_view, list_medics_view

urlpatterns = [
    path(" ", list_medics_view, name='medics'),
    path("favorite", add_favorite_view, name='medic-favorite'),
]
