from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from myapp.myform import BookForm


# Create your views here.
def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})


def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES,instance=Book())
        if form.is_valid():
            form.save()

        if form.is_valid():
            book=form.save()
            messages.success(request, f'{book.title} Successfully added')
            return redirect('show_books')
    else:
            form = BookForm()
    return render(request, 'add_books.html', {'form': form})

    # Book.objects.create(title='The seven tails',
    #                     year=2018,
    #                     category='Fiction',
    #                     cost=750,
    #                     isbn='456789321',
    #                     published=True)
    # Book.objects.create(title='Laws of Power',
    #                     year=2010,
    #                     category='strategy',
    #                     cost=900,
    #                     isbn='123987654',
    #                     published=True, )
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.warning(request, f'{book.title} Successfully deleted')
    return redirect('show_books')

def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title}  Successfully edited')
            return redirect('show_books')
    else:
            form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

#   TODO  upload image, login, register, django admin

