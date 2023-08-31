from django.shortcuts import render
from rest_framework import viewsets, views
from .models import Author, Address, Student, Book, BookIssued, BookReturned
from .serializers import AuthorSerializer, AddressSerializer, StudentSerializer, BookSerializer, BookIssuedSerializer, BookReturnedSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
          
class BookIssuedView(viewsets.ModelViewSet):
    queryset = BookIssued.objects.all()
    serializer_class = BookIssuedSerializer

class BookReturnedView(viewsets.ModelViewSet):
    queryset = BookReturned.objects.all()
    serializer_class = BookReturnedSerializer