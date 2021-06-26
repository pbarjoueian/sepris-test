from django.urls import include, path
from rest_framework import routers

from .api import AuthorViewSet, BookViewSet, PublicationViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'publication', PublicationViewSet, basename='publication')


urlpatterns = [
    path('', include(router.urls)),
]
