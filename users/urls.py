from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet
from post.views import PostCreateView, PostGetView, PostsView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
