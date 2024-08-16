from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
import uuid


class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": str(uuid.uuid4())[:13],
            "language": "en",
            "published_date": "2022-01-01"
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        new_book_data = {
            "title": "Another Test Book",
            "author": "Another Test Author",
            "isbn": str(uuid.uuid4())[:13],
            "language": "en"
        }

        response = self.client.post(
            '/api/books/', new_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('isbn', response.data)

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_id(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_update_book(self):
        updated_book_data = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "isbn": self.book.isbn,
            "language": "fr"
        }

        response = self.client.put(
            f'/api/books/{self.book.id}/', updated_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_book_data["title"])
        self.assertEqual(self.book.language, updated_book_data["language"])

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pagination(self):
        for i in range(20):
            Book.objects.create(
                title=f"Book {i}",
                author="Test Author",
                isbn=str(uuid.uuid4())[:13],
                language="en"
            )

        response = self.client.get('/api/books/?page=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_filter_books_by_author(self):
        response = self.client.get('/api/books/?author=Test Author')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_books_by_published_date(self):
        response = self.client.get('/api/books/?published_date=2022-01-01')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_books_by_language(self):
        response = self.client.get('/api/books/?language=en')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
