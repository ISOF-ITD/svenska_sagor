from django.conf.urls import include, url

urlpatterns = [

    url(r'^records_placess/', include('sagenkarta_admin.urls.records_places_urls')),  # NOQA
    url(r'^socken_v1_s/', include('sagenkarta_admin.urls.socken_v1_urls')),
    url(r'^records_personss/', include('sagenkarta_admin.urls.records_persons_urls')),
    url(r'^recordss/', include('sagenkarta_admin.urls.records_urls')),
    url(r'^medias/', include('sagenkarta_admin.urls.media_urls')),
    url(r'^persons_placess/', include('sagenkarta_admin.urls.persons_places_urls')),
    url(r'^personss/', include('sagenkarta_admin.urls.persons_urls')),
    url(r'^sockens/', include('sagenkarta_admin.urls.socken_urls')),
    url(r'^records_medias/', include('sagenkarta_admin.urls.records_media_urls')),
    url(r'^records_categorys/', include('sagenkarta_admin.urls.records_category_urls')),
    url(r'^categories_klintbergs/', include('sagenkarta_admin.urls.categories_klintberg_urls')),
    url(r'^categoriess/', include('sagenkarta_admin.urls.categories_urls')),
    url(r'^harads/', include('sagenkarta_admin.urls.harad_urls')),
]
