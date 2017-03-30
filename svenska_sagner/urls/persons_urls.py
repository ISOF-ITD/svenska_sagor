from django.conf.urls import url
from ..views import (PersonsListView, PersonsCreateView, PersonsDetailView,
                     PersonsUpdateView, PersonsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PersonsCreateView.as_view()),
        name="persons_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PersonsUpdateView.as_view()),
        name="persons_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PersonsDeleteView.as_view()),
        name="persons_delete"),

    url(r'^(?P<pk>\d+)/$',
        PersonsDetailView.as_view(),
        name="persons_detail"),

    url(r'^$',
        PersonsListView.as_view(),
        name="persons_list"),
]
