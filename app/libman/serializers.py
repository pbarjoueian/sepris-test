from rest_framework import serializers

from .models import Author, Book, Publicaition


class PublicaitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaition
        fields = ('id', 'name', 'phone_number', 'address', 'created_by',
                  'created_at', 'updated_at')

        read_only_fields = ['created_by']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'nick_name', 'created_by',
                  'created_at', 'updated_at')

        read_only_fields = ['created_by']


class BookSerializer(serializers.ModelSerializer):
    published_by = PublicaitionSerializer(read_only=True)
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'page_number', 'publication_year', 'published_by', 'author', 'created_by',
                  'created_at', 'updated_at')

        read_only_fields = ['created_by']
