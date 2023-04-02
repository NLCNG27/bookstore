# bookstore/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookstoreTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Book title",
            author="Cool author",
            year="2023",
        )

    def test_book_model(self):
        self.assertEqual(self.book.title, "Book title")
        self.assertEqual(self.book.author, "Cool author")
        self.assertEqual(self.book.year, "2023")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cool author")
        self.assertTemplateUsed(response, "home.html")