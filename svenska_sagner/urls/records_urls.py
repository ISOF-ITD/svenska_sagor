from django.conf.urls import url
from ..views import (RecordsListView, RecordsCreateView, RecordsDetailView,
                     RecordsUpdateView, RecordsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RecordsCreateView.as_view()),
        name="records_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RecordsUpdateView.as_view()),
        name="records_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RecordsDeleteView.as_view()),
        name="records_delete"),

    url(r'^(?P<pk>\d+)/$',
        RecordsDetailView.as_view(),
        name="records_detail"),

    url(r'^$',
        RecordsListView.as_view(),
        name="records_list"),
]
