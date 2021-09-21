
from django.urls import path

from .views import PostViewSet, UploadView


urlpatterns = [
    path('post/', PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
        })),
    path('upload', UploadView.as_view()),
]