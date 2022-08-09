from rest_framework import serializers
from books.models import Book, BookItem, Author



class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Author
        fields=['id','name','description']



class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookItem
        fields=['name','description']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    authorId =serializers.PrimaryKeyRelatedField(write_only=True, queryset=Author.objects.all(), source='author')
    class Meta:
        model=Book
        fields=['title','subject','publisher','language','numberOfPages','author','authorId']