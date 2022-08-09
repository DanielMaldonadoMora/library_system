from rest_framework import serializers
from books.models import Book, BookItem, Author
from library_sys.models import Rack
from library_sys.api.serializers import RackSerializer



class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Author
        fields=['id','name','description']



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    authorId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=Author.objects.all(), source='author')
    class Meta:
        model=Book
        fields=['title','subject','publisher','language','numberOfPages','author','authorId']


class BookItemSerializer(serializers.ModelSerializer):
    bookInfo = BookSerializer(read_only=True)
    bookId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=Book.objects.all(), source='bookInfo')
    rack = RackSerializer(read_only=True)
    rackId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=Rack.objects.all(), source='rack')
    class Meta:
        model=BookItem
        fields=['barcode','bookInfo','rack','bookId','rackId','status']