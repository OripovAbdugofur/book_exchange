from django import forms
from .models import Book, ExchangeRequest

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ExchangeRequestForm(forms.ModelForm):
    class Meta:
        model = ExchangeRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Sizning kitobingiz haqida qisqacha...'}),
        }