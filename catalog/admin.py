from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name',
              ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'display_status', 'borrower', 'due_back', 'id')
    list_filter = ("book__language", "status", "book")
    fieldsets = (
        ('Book Information', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Status', {
            'fields': ('status','due_back', 'borrower')
        }),
    )

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "display_genre", "display_language","display_author")
    list_filter = ("genre", "author", "language")
    inlines = [BookInstanceInline]

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)



