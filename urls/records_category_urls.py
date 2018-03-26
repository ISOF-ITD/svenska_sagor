from django.conf.urls import url
from ..views import (RecordsCategoryListView, RecordsCategoryCreateView, RecordsCategoryDetailView,
                     RecordsCategoryUpdateView, RecordsCategoryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RecordsCategoryCreateView.as_view()),
        name="records_category_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RecordsCategoryUpdateView.as_view()),
        name="records_category_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RecordsCategoryDeleteView.as_view()),
        name="records_category_delete"),

    url(r'^(?P<pk>\d+)/$',
        RecordsCategoryDetailView.as_view(),
        name="records_category_detail"),

    url(r'^$',
        RecordsCategoryListView.as_view(),
        name="records_category_list"),
]
