from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.AdminDashView.as_view(), name='ad_dash'),
    path('tc', views.TeacherDashView.as_view(), name='tc_dash'),
    path('pt', views.ParentDashView.as_view(), name='pt_dash'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
