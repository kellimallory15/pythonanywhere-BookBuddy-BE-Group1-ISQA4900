from django.contrib import admin
from .models import Reader, Book, Author, Review, BookBuddy

class ReaderList(admin.ModelAdmin):
    list_display = ('pk','reader_num', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'created_date', 'updated_date')
    list_filter = ('reader_num', 'name', 'city')
    search_fields = ('reader_num', 'name')
    ordering = ['reader_num']

class BookList(admin.ModelAdmin):
    list_display = ('author', 'book_num', 'genre', 'summary', 'publisher', 'published_date', 'page_total', 'title')
    list_filter = ('author', 'genre', 'book_num')
    search_fields = ('book_num', 'author', 'genre')
    ordering = ['book_num']

class AuthorList(admin.ModelAdmin):
    list_display = ('name','photo', 'birth_date', 'death_date', 'auth_id')
    list_filter = ('name','auth_id')
    search_fields = ('name', 'auth_id')
    ordering = ['auth_id']

class ReviewList(admin.ModelAdmin):
    list_display = ('book', 'reader', 'title', 'text', 'rating', 'created_date', 'edited_date')
    list_filter = ('book', 'rating', 'title')
    search_fields = ('book', 'title')
    ordering = ['book']

class BookBuddyList(admin.ModelAdmin):
    list_display = ('book', 'reader', 'fav_status', 'read_status', 'read_later_status', 'currently_reading', 'current_page', 'last_read')
    list_filter = ('book', 'reader', 'read_status', 'fav_status')
    search_fields = ('book', 'fav_status', 'reader')
    ordering = ['book']

admin.site.register(Reader, ReaderList)
admin.site.register(Book, BookList)
admin.site.register(Author, AuthorList)
admin.site.register(Review, ReviewList)
admin.site.register(BookBuddy, BookBuddyList)

