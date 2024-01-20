from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'author', 'publishing_date', 'publisher', 'category', 'distribution_expenses']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publishing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'distribution_expenses': forms.NumberInput(attrs={'class': 'form-control'}),
        }
