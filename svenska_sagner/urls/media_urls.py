from django.conf.urls import url
from ..views import (MediaListView, MediaCreateView, MediaDetailView,
                     MediaUpdateView, MediaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(MediaCreateView.as_view()),
        name="media_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(MediaUpdateView.as_view()),
        name="media_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(MediaDeleteView.as_view()),
        name="media_delete"),

    url(r'^(?P<pk>\d+)/$',
        MediaDetailView.as_view(),
        name="media_detail"),

    url(r'^$',
        MediaListView.as_view(),
        name="media_list"),
]
