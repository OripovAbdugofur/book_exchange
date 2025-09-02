from django.contrib import admin
from .models import Book, ExchangeRequest

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'owner', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'author')

@admin.register(ExchangeRequest)
class ExchangeRequestAdmin(admin.ModelAdmin):
    list_display = ('book', 'requester', 'status', 'created_at')
    list_filter = ('status', 'created_at')