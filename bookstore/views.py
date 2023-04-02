# bookstore/views.py
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Book

class BookstoreListView(ListView):
    model = Book
    template_name = "home.html"


class BookstoreCreateView(CreateView):
    model = Book
    template_name = "book_new.html"
    fields = ["title", "author", "year"]
