from django.conf.urls import url
from ..views import (RecordsMediaListView, RecordsMediaCreateView, RecordsMediaDetailView,
                     RecordsMediaUpdateView, RecordsMediaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RecordsMediaCreateView.as_view()),
        name="records_media_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RecordsMediaUpdateView.as_view()),
        name="records_media_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RecordsMediaDeleteView.as_view()),
        name="records_media_delete"),

    url(r'^(?P<pk>\d+)/$',
        RecordsMediaDetailView.as_view(),
        name="records_media_detail"),

    url(r'^$',
        RecordsMediaListView.as_view(),
        name="records_media_list"),
]
