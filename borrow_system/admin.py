from django.contrib import admin
from borrow_system.models import Borrow

# Register your models here.
@admin.register(Borrow)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['user','book','borrowed']