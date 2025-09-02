from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Mavjud'),
        ('exchanged', 'Almashilgan'),
        ('requested', 'So\'ralgan'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title


class ExchangeRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('accepted', 'Qabul qilindi'),
        ('rejected', 'Rad etildi'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username} - {self.book.title}"