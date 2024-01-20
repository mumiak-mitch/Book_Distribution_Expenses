# books/admin.py
from django.contrib import admin
from .models import BookCategory, Book

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishing_date', 'category', 'distribution_expenses')
    list_filter = ('category', 'publishing_date')
    search_fields = ('title', 'author')
    date_hierarchy = 'publishing_date'
