# Generated by Django 4.2.4 on 2023-10-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybook', '0011_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
    ]
