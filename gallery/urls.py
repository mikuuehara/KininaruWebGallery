from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'', views.top.as_view(), name='top'),
    #path(r'm', views.register.as_view(), name='manage'),
    path(r'evaluation', views.evaluation.as_view(), name='evaluation'),
    path(r'result', views.result.as_view(), name='result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)