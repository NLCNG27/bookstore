# bookstore/urls.py
from django.urls import path
from .views import BookstoreListView

urlpatterns = [
    path("", BookstoreListView.as_view(), name="home")
]