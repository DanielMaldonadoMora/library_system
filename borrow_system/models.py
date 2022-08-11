from django.db import models
from django.db.models import SET_NULL
from users.models import User
from books.models import BookItem


class Borrow(models.Model):
    user=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    book=models.ForeignKey(BookItem,on_delete=SET_NULL,null=True)
    borrowed=models.DateField(null=True,blank=True)
    dueDate=models.DateField(null=True,blank=True)
    

    def __str__(self):
        return self.title