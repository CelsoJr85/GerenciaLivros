from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Book
from .forms import BookForm
from rest_framework.decorators import api_view
import requests


# Listar livros
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


# Criar livro
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


# Editar livro
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})


# Excluir livro
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})


# Marcar como lido/não lido
def toggle_read_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.read = not book.read
    book.date_read = None if not book.read else book.date_read or date.today()
    book.save()
    return redirect('book_list')
