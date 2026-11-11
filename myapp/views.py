from django.shortcuts import render

# Create your views here.
def show_books(request):
    return render(request, 'show_books.html')


def add_books(request):
    return render(request, 'add_books.html')