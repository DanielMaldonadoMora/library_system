from rest_framework import serializers
from borrow_system.models import Borrow



class BorrowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Borrow
        fields=['user','book','borrowed','dueDate']