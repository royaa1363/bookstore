# Generated by Django 4.2.4 on 2023-08-24 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybook', '0007_alter_nevisande_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nevisande',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='nevisande',
            new_name='author',
        ),
    ]
