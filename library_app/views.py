from django.shortcuts import render
from rest_framework import viewsets, views
from .models import Author, Address, Student, Book, BookIssued, BookReturned
from .serializers import AuthorSerializer, AddressSerializer, StudentSerializer, BookSerializer, BookIssuedSerializer, BookReturnedSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response

class AuthorView(views.APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_ok)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetails(viewsets.ModelViewSet):
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