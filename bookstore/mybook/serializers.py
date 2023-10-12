from rest_framework import serializers

from .models import Book, Author, Category, Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tag = TagSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'
