from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = "gallery"

urlpatterns = [
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
