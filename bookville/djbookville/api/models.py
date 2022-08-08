from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=10, default="")
    
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.SlugField(max_length=50)
    author = models.SlugField(max_length=50)
    isbn = models.CharField(max_length=20)
    publication = models.SlugField(max_length=50)
    pages = models.IntegerField(default=0)
    
    shop = models.ForeignKey("Shop",on_delete=models.CASCADE, related_name="shop")

    def __str__(self):
        return f'{self.title} - {self.author}'

class Shop(models.Model):
    bookstore_name = models.SlugField(max_length=50)
    address = models.CharField(max_length=50)
    town = models.SlugField(max_length=50)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return f'{self.bookstore_name} - {self.owner}'

