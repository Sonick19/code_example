from django import forms

from .models import Book

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
