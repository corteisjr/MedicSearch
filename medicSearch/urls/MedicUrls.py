from  django.urls import path
from medicSearch.views.MedicView import add_favorite_view, list_medics_view, rate_medic_view, remove_favorite_view

urlpatterns = [
    path("", list_medics_view, name='medics'),
    path("favorite", add_favorite_view, name='medic-favorite'),
    path("favorite/remove", remove_favorite_view, name='medic-favorite-remove'),
    path("rating/<int:medic_id>/", rate_medic_view, name='rate-medic')
]
