from django.conf.urls import include, url

urlpatterns = [

    url(r'^records_placess/', include('Sagenkarta-Admin.urls.records_places_urls')),  # NOQA
    url(r'^socken_v1_s/', include('Sagenkarta-Admin.urls.socken_v1_urls')),
    url(r'^records_personss/', include('Sagenkarta-Admin.urls.records_persons_urls')),
    url(r'^recordss/', include('Sagenkarta-Admin.urls.records_urls')),
    url(r'^persons_placess/', include('Sagenkarta-Admin.urls.persons_places_urls')),
    url(r'^personss/', include('Sagenkarta-Admin.urls.persons_urls')),
    url(r'^sockens/', include('Sagenkarta-Admin.urls.socken_urls')),
    url(r'^records_categorys/', include('Sagenkarta-Admin.urls.records_category_urls')),
    url(r'^categories_klintbergs/', include('Sagenkarta-Admin.urls.categories_klintberg_urls')),
    url(r'^categoriess/', include('Sagenkarta-Admin.urls.categories_urls')),
    url(r'^harads/', include('Sagenkarta-Admin.urls.harad_urls')),
]
