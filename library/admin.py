from django.contrib import admin
from library.models import Library,Rack


@admin.register(Library)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Rack)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['library','location','number']