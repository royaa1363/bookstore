from django.db import models


class Nevisande(models.Model):
    author = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f" {self.author}"


class Book(models.Model):
    book_name = models.CharField(max_length=256, null=True)
    nevisande = models.ForeignKey(Nevisande, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f" {self.book_name}"




