from django.urls import path

from .views import ColibriViewSet


urlpatterns = [
    path('colibri/', ColibriViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        })),
]