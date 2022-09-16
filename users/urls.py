from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserPostsViewSet

router = DefaultRouter(trailing_slash = False)

router.register(r'posts', UserPostsViewSet, basename='posts')

urlpatterns = [
    path('api/', include(router.urls))
]

urlpatterns=urlpatterns+router.urls


