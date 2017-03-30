from django.conf.urls import url
from ..views import (PersonsPlacesListView, PersonsPlacesCreateView, PersonsPlacesDetailView,
                     PersonsPlacesUpdateView, PersonsPlacesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PersonsPlacesCreateView.as_view()),
        name="persons_places_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PersonsPlacesUpdateView.as_view()),
        name="persons_places_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PersonsPlacesDeleteView.as_view()),
        name="persons_places_delete"),

    url(r'^(?P<pk>\d+)/$',
        PersonsPlacesDetailView.as_view(),
        name="persons_places_detail"),

    url(r'^$',
        PersonsPlacesListView.as_view(),
        name="persons_places_list"),
]
