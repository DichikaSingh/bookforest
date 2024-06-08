from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('seller','book_name' ,'book_category','sub_category','subject', 'price', 'is_donated', 'entry_date','book_type','picture')
