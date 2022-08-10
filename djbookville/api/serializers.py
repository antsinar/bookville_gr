from imp import source_from_cache
from unicodedata import name
from .models import Book, User, Shop
from rest_framework import serializers
from phonenumber_field.phonenumber import to_python
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PhoneNumberField(serializers.CharField):
    default_error_messages = {"invalid": _("Enter a valid phone number.")}

    def to_internal_value(self, data):
        phone_number = to_python(data)
        if phone_number and not phone_number.is_valid():
            raise ValidationError(self.error_messages["invalid"])
        return phone_number

class BookSerializer(serializers.ModelSerializer):
    title = serializers.SlugField(max_length=50)
    author = serializers.SlugField(max_length=50)
    isbn = serializers.CharField(max_length=20)
    publication = serializers.SlugField(max_length=50)
    pages = serializers.IntegerField(default=0)
    shop = serializers.CharField(source="shop.bookstore_name")
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'isbn',
            'publication',
            'pages',
            'shop'
        )

class ShopSerializer(serializers.ModelSerializer):
    bookstore_name = serializers.SlugField(max_length=50)
    address = serializers.CharField(max_length=50)
    town = serializers.SlugField(max_length=50)
    owner = serializers.CharField(source="owner.username")
    
    class Meta:
        model = Shop
        fields = (
            "bookstore_name",
            "address",
            "town",
            "owner"
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        )