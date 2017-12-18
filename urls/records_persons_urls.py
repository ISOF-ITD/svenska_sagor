from django.conf.urls import url
from ..views import (RecordsPersonsListView, RecordsPersonsCreateView, RecordsPersonsDetailView,
                     RecordsPersonsUpdateView, RecordsPersonsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RecordsPersonsCreateView.as_view()),
        name="records_persons_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RecordsPersonsUpdateView.as_view()),
        name="records_persons_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RecordsPersonsDeleteView.as_view()),
        name="records_persons_delete"),

    url(r'^(?P<pk>\d+)/$',
        RecordsPersonsDetailView.as_view(),
        name="records_persons_detail"),

    url(r'^$',
        RecordsPersonsListView.as_view(),
        name="records_persons_list"),
]
