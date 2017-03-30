from django.conf.urls import url
from ..views import (SockenV1ListView, SockenV1CreateView, SockenV1DetailView,
                     SockenV1UpdateView, SockenV1DeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SockenV1CreateView.as_view()),
        name="socken_v1_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SockenV1UpdateView.as_view()),
        name="socken_v1_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SockenV1DeleteView.as_view()),
        name="socken_v1_delete"),

    url(r'^(?P<pk>\d+)/$',
        SockenV1DetailView.as_view(),
        name="socken_v1_detail"),

    url(r'^$',
        SockenV1ListView.as_view(),
        name="socken_v1_list"),
]
