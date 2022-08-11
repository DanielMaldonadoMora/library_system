from rest_framework import serializers
from books.models import Book, BookItem, Author
from library_sys.models import Rack,Library
from library_sys.api.serializers import RackSerializer, LibrarySerializer



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
    library = LibrarySerializer(read_only=True)
    libraryId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=Library.objects.all(), source='library')
    class Meta:
        model=BookItem
        fields=['id','barcode','bookInfo','bookId','library','libraryId','rack','rackId','status',]