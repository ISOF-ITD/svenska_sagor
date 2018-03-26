from django.conf.urls import url
from ..views import (CategoriesListView, CategoriesCreateView, CategoriesDetailView,
                     CategoriesUpdateView, CategoriesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CategoriesCreateView.as_view()),
        name="categories_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CategoriesUpdateView.as_view()),
        name="categories_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CategoriesDeleteView.as_view()),
        name="categories_delete"),

    url(r'^(?P<pk>\d+)/$',
        CategoriesDetailView.as_view(),
        name="categories_detail"),

    url(r'^$',
        CategoriesListView.as_view(),
        name="categories_list"),
]
