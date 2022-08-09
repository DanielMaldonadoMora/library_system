from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from library.models import Library,Rack
from library.api.serializers import RackSerializer,LibrarySerializer
from library.api.permissions import IsAdminOrReadOnly


class LibraryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = LibrarySerializer
    queryset = Library.objects.all() 
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['name'] 

class RackApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = RackSerializer
    queryset = Rack.objects.all() 
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['id','number','location','library'] 
    