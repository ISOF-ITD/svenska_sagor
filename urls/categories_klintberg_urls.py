from django.conf.urls import url
from ..views import (CategoriesKlintbergListView, CategoriesKlintbergCreateView, CategoriesKlintbergDetailView,
                     CategoriesKlintbergUpdateView, CategoriesKlintbergDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CategoriesKlintbergCreateView.as_view()),
        name="categories_klintberg_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CategoriesKlintbergUpdateView.as_view()),
        name="categories_klintberg_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CategoriesKlintbergDeleteView.as_view()),
        name="categories_klintberg_delete"),

    url(r'^(?P<pk>\d+)/$',
        CategoriesKlintbergDetailView.as_view(),
        name="categories_klintberg_detail"),

    url(r'^$',
        CategoriesKlintbergListView.as_view(),
        name="categories_klintberg_list"),
]
