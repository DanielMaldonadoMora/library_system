from django.db import models
from django.db.models import SET_NULL
#from library.models import Rack

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
    borrowed=models.DateField()
    dueDate=models.DateField()
    status=models.CharField(max_length=255)
    bookInfo=models.ForeignKey(Book,on_delete=SET_NULL,null=True)
    #location=models.ForeignKey(Rack,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.status
    