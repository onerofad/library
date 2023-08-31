from django.contrib import admin
from .models import Author, Address, Student, Book, BookIssued, BookReturned

admin.site.register({Author, Address, Student, Book, BookIssued, BookReturned})