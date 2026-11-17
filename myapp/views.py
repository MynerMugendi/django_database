from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login

from myapp.models import Book
from myapp.myform import BookForm, RegisterForm


# Create your views here.
@login_required
def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})


@login_required
@permission_required('myapp.add_book', raise_exception=True)
def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book {request.POST.get('title')}Successfully added")
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


@login_required
@permission_required('myapp.delete_book', raise_exception=True)
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.warning(request, f'{book.title} Successfully deleted')
    return redirect('show_books')


@login_required
@permission_required('myapp.change_book', raise_exception=True)
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title}  Successfully edited')
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


#   TODO  upload image, login, register, django admin

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('show_books')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

# python manage.py createsuperuser
