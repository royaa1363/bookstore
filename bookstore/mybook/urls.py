from rest_framework import routers
from django.urls import path, include

from .views import BooksViewSet, AuthorViewSet, CategoryViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('books', BooksViewSet)
router.register('author', AuthorViewSet)
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
