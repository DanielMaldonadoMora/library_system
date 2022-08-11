from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from borrow_system.api.permissions import PermissionBorrowView
from borrow_system.api.serializers import BorrowSerializer
from borrow_system.models import Borrow



class BorrowApiViewSet(ModelViewSet):
    permission_classes = [PermissionBorrowView]
    serializer_class = BorrowSerializer
    queryset = Borrow.objects.all() 
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['id','book','user'] 