from django.conf.urls import url
from ..views import (HaradListView, HaradCreateView, HaradDetailView,
                     HaradUpdateView, HaradDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(HaradCreateView.as_view()),
        name="harad_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(HaradUpdateView.as_view()),
        name="harad_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(HaradDeleteView.as_view()),
        name="harad_delete"),

    url(r'^(?P<pk>\d+)/$',
        HaradDetailView.as_view(),
        name="harad_detail"),

    url(r'^$',
        HaradListView.as_view(),
        name="harad_list"),
]
