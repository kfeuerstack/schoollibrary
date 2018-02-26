from django.db import models
from django.urls import reverse #Used to generate URLs
import uuid

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter book genre (e.g. Fiction, Nonfiction, Poetry etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Description of book')
    isbn = models.CharField('ISBN', max_length=13, help_text='Enter ISBN')
    genre = models.ManyToManyField(Genre, help_text='Select genre') #ManyToManyField used as genres can contain any number of books

    def __str__(self):
        return self.title
        #Uses a book's title to represent a boook record

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
        #Returns the URL to access a book's details

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    #Model that represents a specific copy of a book
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique Book ID")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '{0} ({1})'.format(self.id,self.book.title)



class Author(models.Model):
    #Model that represents authors
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        #Returns URL for an author
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name,self.first_name)
