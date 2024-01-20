from django.db import models
from django.urls import reverse

class BookCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse('book_list') 
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255)
    publishing_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey('BookCategory', on_delete=models.CASCADE, null=True, blank=True)
    distribution_expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
