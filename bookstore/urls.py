# bookstore/urls.py
from django.urls import path
from .views import BookstoreListView, BookstoreCreateView

urlpatterns = [
    path("book/new/", BookstoreCreateView.as_view(), name="book_new"),
    path("", BookstoreListView.as_view(), name="home"),
]