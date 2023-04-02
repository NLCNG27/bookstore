# bookstore/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Book


class BookstoreListView(ListView):
    model = Book
    template_name = "home.html"
    paginate_by = 10                # specify max number in a page for pagination


class BookstoreDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookstoreCreateView(CreateView):
    model = Book
    template_name = "book_new.html"
    fields = ["title", "author", "year"]
    success_url = reverse_lazy("home")


class BookstoreUpdateView(UpdateView):
    model = Book
    template_name = "book_edit.html"
    fields = ["title", "author", "year"]


class BookstoreDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("home")
