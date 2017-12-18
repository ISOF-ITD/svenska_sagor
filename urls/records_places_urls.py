from django.conf.urls import url
from ..views import (RecordsPlacesListView, RecordsPlacesCreateView, RecordsPlacesDetailView,
                     RecordsPlacesUpdateView, RecordsPlacesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RecordsPlacesCreateView.as_view()),
        name="records_places_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RecordsPlacesUpdateView.as_view()),
        name="records_places_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RecordsPlacesDeleteView.as_view()),
        name="records_places_delete"),

    url(r'^(?P<pk>\d+)/$',
        RecordsPlacesDetailView.as_view(),
        name="records_places_detail"),

    url(r'^$',
        RecordsPlacesListView.as_view(),
        name="records_places_list"),
]
