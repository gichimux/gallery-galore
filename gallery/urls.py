from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^search/',views.search_images,name='search_results'),
    url(r'^location/(\d+)',views.filter_location,name='located_images')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)     