"""
Django URLs for serving the game
"""
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', TemplateView.as_view(template_name='vanilla.html'), name='game'),
    re_path(r'^textures/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR / 'textures'}),
    re_path(r'^(?P<path>.+\.png)$', serve, {'document_root': settings.BASE_DIR}),
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR)
