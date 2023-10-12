from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f" {self.author}"


class Category(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    title = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f'{self.title}'


class Book(models.Model):
    book_name = models.CharField(max_length=256, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    pub_date = models.DateField("date published")

    def __str__(self):
        return f" {self.book_name}"
