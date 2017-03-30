from django.conf.urls import include, url

urlpatterns = [

    url(r'^records_placess/', include('svenska_sagner.urls.records_places_urls')),  # NOQA
    url(r'^socken_v1_s/', include('svenska_sagner.urls.socken_v1_urls')),
    url(r'^records_personss/', include('svenska_sagner.urls.records_persons_urls')),
    url(r'^recordss/', include('svenska_sagner.urls.records_urls')),
    url(r'^medias/', include('svenska_sagner.urls.media_urls')),
    url(r'^persons_placess/', include('svenska_sagner.urls.persons_places_urls')),
    url(r'^personss/', include('svenska_sagner.urls.persons_urls')),
    url(r'^sockens/', include('svenska_sagner.urls.socken_urls')),
    url(r'^records_medias/', include('svenska_sagner.urls.records_media_urls')),
    url(r'^records_categorys/', include('svenska_sagner.urls.records_category_urls')),
    url(r'^categories_klintbergs/', include('svenska_sagner.urls.categories_klintberg_urls')),
    url(r'^categoriess/', include('svenska_sagner.urls.categories_urls')),
    url(r'^harads/', include('svenska_sagner.urls.harad_urls')),
]
