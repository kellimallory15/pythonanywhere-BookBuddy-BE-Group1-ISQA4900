from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

## Need to potentially update model and add definitions for various string returns once front end built
class Reader(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='readers')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    reader_num = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

class Author(models.Model):
    birth_date = models.DateField(default=timezone.now)
    death_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=50)
    auth_id = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name ## Potentially specify different retrun

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='book_authors')
    book_num = models.IntegerField(blank=False, null=False)
    genre = models.CharField(max_length=50)
    summary = models.CharField(max_length=500)
    publisher = models.CharField(max_length=50)
    published_date = models.DateField(default=timezone.now)
    page_total = models.IntegerField(blank=False, default=0, null=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.author)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, related_name='book_review')
    reader = models.ForeignKey(Reader, on_delete=models.RESTRICT, related_name='reader_review')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    rating = models.IntegerField(blank=False, null=False, default=1,
                                 validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_date = models.DateField(default=timezone.now)
    edited_date = models.DateField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.edited_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self) ##define output potentially

    def reader_reviews(self):
        return str(self.reader.reader_num)

class BookBuddy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, related_name='buddy_book')
    reader = models.ForeignKey(Reader, on_delete=models.RESTRICT, related_name='buddy_reader')
    fav_status = models.BooleanField(default=False, null=True)
    read_status = models.BooleanField(default=False, null=True)
    read_later_status = models.BooleanField(default=False, null=True)
    currently_reading = models.BooleanField(default=False, null=True)
    current_page = models.IntegerField(default=0, null=True, blank=False)
    last_read = models.DateField(default=timezone.now)

    def updated(self):
        self.last_read = timezone.now()
        self.save()

    def __str__(self):
        return str(self)


    ## Define null statuses for above booleans // identify date modifications required for last read

