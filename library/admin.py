from django.contrib import admin
from .models import Book, Author, BorrowRecord

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'available')
    list_filter = ('author', 'published_date')
    search_fields = ('title',)

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('borrower',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)