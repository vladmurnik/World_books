from django.db import models
from django.urls import reverse
from django.db.models import Count
from django.contrib.auth.models import User
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=200,
    help_text = "Enter the genre of the book",
                            verbose_name = "Genre")

    def __str__(self):
        return f"{self.name} ({self.book_set.count()})"

class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text = "Enter the language of the book",
                            verbose_name = "Language")
    def __str__(self):
        return f"{self.name} ({self.book_set.count()})"

class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text = "Enter the first name of the author",
                                  verbose_name = "Name of Author")
    last_name = models.CharField(max_length=100,
                                 help_text = "Enter the last name of the author",
                                 verbose_name = "Family Name of Author")
    date_of_birth = models.DateField(help_text = "Enter the date of birth of the author",
                                     verbose_name = "Date of Birth",
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text = "Enter the date of death of the author",
                                     verbose_name = "Date of Death",
                                     null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.book_set.count()})"

class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text = "Enter the title of the book",
                             verbose_name = "Title")

    genre = models.ForeignKey('Genre',
                              on_delete=models.CASCADE,
                              help_text="Enter the genre of the book",
                              verbose_name="Genre",
                              null=True)

    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 help_text="Enter the language of the book",
                                 verbose_name="Language",
                                 null=True)

    author = models.ManyToManyField('Author',
                                    help_text="Enter the author of the book",
                                    verbose_name="Author",)

    summary = models.TextField(max_length=1000,
                               help_text="Enter the summary of the book",
                               verbose_name="Summary",)

    isbn = models.CharField(max_length=13,
                            help_text="Enter the ISBN of the book",
                            verbose_name="ISBN",)

    def display_author(self):
        return ', '.join([f"{author.last_name} {author.first_name}" for author in self.author.all()])
    display_author.short_description = "Author"

    def display_language(self):
        return self.language.name

    def display_genre(self):
        return self.genre.name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text = "Enter the status of the book",
                            verbose_name = "Status",
    )

    def filter_status(self):
        return self.name

    def __str__(self):
        return f"{self.name} ({self.bookinstance_set.count()})"

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True,)

    inv_nom = models.CharField(max_length=20, null=True,
                               help_text="Enter the inverter number of the book",
                               verbose_name = "Inverter Number",)

    imprint = models.CharField(max_length=200,
                               help_text="Enter the publisher and year of publication",
                               verbose_name = "Publisher",)

    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=True,
                               help_text="Changing instance status",
                               verbose_name = "Status",)

    due_back = models.DateField(null=True, blank=True,
                                help_text="Enter the due date of the book",
                                verbose_name = "Due Date",)

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null = True, blank = True,
                                 verbose_name = "Borrower",
                                 help_text = "Enter the borrower of the book",)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def display_status(self):
        return self.status.name

    def __str__(self):
        return '%s| %s| %s' % (self.inv_nom, self.book, self.status.filter_status())