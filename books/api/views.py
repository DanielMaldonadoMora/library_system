from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from books.models import Book, BookItem, Author
from books.api.serializers import AuthorSerializer,BookSerializer,BookItemSerializer
from books.api.permissions import IsAdminOrReadOnly


class AuthorApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.all() 
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['name','description'] 

class BooksApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all() 
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['title','subject','publisher','language'] 
    