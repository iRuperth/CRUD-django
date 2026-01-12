from django.contrib import admin
from .models import Book

@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'publisher_date', 'isbn')
    search_fields = ('name', 'author', 'isbn')
    list_filter = ('author', 'publisher_date')
    list_per_page = 10