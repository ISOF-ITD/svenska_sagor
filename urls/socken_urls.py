from django.conf.urls import url
from ..views import (SockenListView, SockenCreateView, SockenDetailView,
                     SockenUpdateView, SockenDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(SockenCreateView.as_view()),
        name="socken_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(SockenUpdateView.as_view()),
        name="socken_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(SockenDeleteView.as_view()),
        name="socken_delete"),

    url(r'^(?P<pk>\d+)/$',
        SockenDetailView.as_view(),
        name="socken_detail"),

    url(r'^$',
        SockenListView.as_view(),
        name="socken_list"),
]
