from rest_framework import serializers
from .models import Author, Address, Student, Book, BookIssued, BookReturned

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'about')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields=('mobileno', 'line1', 'line2', 'city', 'state', 'zipcode')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'firstname', 'lastname', 'dob', 'address')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name', 'pub_date', 'no_pages', 'book_lang', 'book_dim', 'book_isbn10', 'book_isbn13', 'author', 'book_issued')

class BookIssuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssued
        fields = ('dateissued', 'book', 'student')

class BookReturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReturned
        fields = ('datereturned', 'book', 'student')