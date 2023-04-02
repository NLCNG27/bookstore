# bookstore/urls.py
from django.urls import path
from .views import BookstoreListView, BookstoreCreateView, BookstoreUpdateView, BookstoreDetailView, BookstoreDeleteView

urlpatterns = [
    path("book/new/", BookstoreCreateView.as_view(), name="book_new"),
    path("book/<int:pk>/", BookstoreDetailView.as_view(), name="book_detail"),
    path("book/<int:pk>/edit", BookstoreUpdateView.as_view(), name="book_edit"),
    path("book/<int:pk>/delete", BookstoreDeleteView.as_view(), name="book_delete"),
    path("", BookstoreListView.as_view(), name="home"),
]