from django.core.files.storage import FileSystemStorage
from django.db import models

def book_upload_to(instance, filename):
    return 'book/{filename}'.format(filename=filename)

def author_upload_to(instance, filename):
    return 'library_app/media/author/{filename}'.format(filename=filename)

fs = FileSystemStorage(location = "authors")


class Author(models.Model):
    name = models.CharField(max_length=400, unique=True)
    about = models.TextField()
    # author_image = models.ImageField(storage=fs)

    def __str__(self):
        return self.name 
    
class Address(models.Model):
    mobileno = models.CharField(max_length=14, unique=True)
    line1 = models.TextField()
    line2 = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return f'{self.city}, {self.state}'
    
class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, to_field='mobileno')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class Book(models.Model):   
    name = models.CharField(max_length=400, unique=True)   
    pub_date = models.DateField()
    no_pages = models.IntegerField()
    book_lang = models.CharField(max_length=400)
    book_dim = models.CharField(max_length=200)
    book_isbn10 = models.CharField(max_length=400, default='Null')
    book_isbn13 = models.CharField(max_length=400, default='Null')
    book_image = models.TextField(default="null")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='name')
    book_issued = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
        
class BookIssued(models.Model):
    dateissued = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Books Issued'

    def __str__(self):
        bk = Book.objects.get(name = self.book.name)
        bk.book_issued = True
        bk.save()

        return self.book.name

    
class BookReturned(models.Model):
    datereturned = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Books Returned'

    def __str__(self):
        return self.book.name