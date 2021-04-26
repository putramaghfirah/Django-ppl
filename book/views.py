from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book

# Create your views here.


class BookList(ListView):
    template_name = 'book/index.html'
    model = Book
    paginate_by = 1  # if pagination is desired
