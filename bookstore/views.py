# bookstore/views.py
from django.views.generic import ListView
from .models import Book

class BookstoreListView(ListView):
    model = Book
    template_name = "home.html"
