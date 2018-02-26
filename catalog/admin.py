from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
