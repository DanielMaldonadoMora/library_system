from rest_framework.routers import DefaultRouter
from books.api.views import AuthorApiViewSet,BooksApiViewSet

router_author = DefaultRouter()
router_books = DefaultRouter()

router_author.register(prefix='author', basename='author', viewset=AuthorApiViewSet)
router_books.register(prefix='books', basename='books', viewset=BooksApiViewSet)