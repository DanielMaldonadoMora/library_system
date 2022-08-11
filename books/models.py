from django.db import models
from django.db.models import SET_NULL, CASCADE
from library_sys.models import Rack,Library

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    language=models.CharField(max_length=255)
    numberOfPages=models.IntegerField()
    author=models.ForeignKey(Author,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.title


class BookItem(models.Model):
    barcode=models.CharField(max_length=255)
    isReferenceOnly=models.BooleanField()
    checkout=models.BooleanField()
    status=models.BooleanField(default=True)
    bookInfo=models.ForeignKey(Book,on_delete=CASCADE ,null=True)
    rack=models.ForeignKey(Rack,on_delete=SET_NULL,null=True) 
    library=models.ForeignKey(Library,on_delete=SET_NULL,null=True) 

    def __str__(self):
        return self.bookInfo.title
    