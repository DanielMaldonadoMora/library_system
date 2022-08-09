from django.db import models
from django.db.models import SET_NULL

# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Rack(models.Model):
    number=models.IntegerField()
    location=models.CharField(max_length=255)
    library=models.ForeignKey(Library, on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.location