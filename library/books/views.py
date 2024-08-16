from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    page_size = 10


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['author', 'published_date', 'language']
