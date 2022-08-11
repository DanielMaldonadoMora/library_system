from django.db import models
from django.db.models import SET_NULL
from users.models import User
from books.models import BookItem



class Borrow(models.Model):
    user=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    book=models.ForeignKey(BookItem,on_delete=SET_NULL,null=True)
    borrowed=models.DateField(auto_now_add=True)
    
    

    def __str__(self):
        return f'{self.book.bookInfo.title} borrowed to {self.user}'