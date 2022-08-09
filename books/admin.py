from django.contrib import admin
from books.models import Book,BookItem,Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name']
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title']
@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display=['bookInfo']