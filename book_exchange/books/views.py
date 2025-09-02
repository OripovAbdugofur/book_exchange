from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, ExchangeRequest
from .forms import BookForm, ExchangeRequestForm

def home(request):
    recent_books = Book.objects.filter(status='available')[:6]
    return render(request, 'books/home.html', {'recent_books': recent_books})

def book_list(request):
    books = Book.objects.filter(status='available')
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def request_exchange(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ExchangeRequestForm(request.POST)
        if form.is_valid():
            exchange_request = form.save(commit=False)
            exchange_request.book = book
            exchange_request.requester = request.user
            exchange_request.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ExchangeRequestForm()
    return render(request, 'books/request_exchange.html', {'form': form, 'book': book})