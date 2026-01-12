from django.shortcuts import render
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})
    
def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})

def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})