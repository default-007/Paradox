from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ad_dash, name='ad_dash'),
    path('tc', views.tc_dash, name='tc_dash'),
    path('pt', views.pt_dash, name='pt_dash'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
