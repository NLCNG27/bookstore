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


    def test_book_createview(self):
        response = self.client.post(
            reverse("book_new"),
            {
                "title": "New title",
                "author": "Nguyen",
                "year": 2023,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, "New title")
        self.assertEqual(Book.objects.last().author, "Nguyen")

    def test_book_updateview(self):
        response = self.client.post(
            reverse("book_edit", args="1"),
            {
                "title": "Updated title",
                "author": "Updated author",
                "year": 2025,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, "Updated title")
        self.assertEqual(Book.objects.last().author, "Updated author")
        self.assertEqual(Book.objects.last().year, 2025)

    def test_book_deleteview(self):
        response = self.client.post(reverse("book_delete", args="1"))
        self.assertEqual(response.status_code, 302)