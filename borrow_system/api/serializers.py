from rest_framework import serializers
from borrow_system.models import Borrow
from users.models import User
from books.models import BookItem
from books.api.serializers import BookItemSerializer
from users.api.serializers import UserSerializer


class BorrowSerializer(serializers.ModelSerializer):
    book = BookItemSerializer(read_only=True)
    bookId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=BookItem.objects.all(), source='bookItem')
    user = UserSerializer(read_only=True)
    userId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')    
    class Meta:
        model=Borrow
        fields=['user','userId','book','bookId','borrowed']