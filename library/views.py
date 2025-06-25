from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Author, BorrowRecord
from .forms import BookForm, AuthorForm
from .export import export_to_excel

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})

def export_books(request):
    response = export_to_excel()
    return HttpResponse(response, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')