# Generated by Django 4.2 on 2023-09-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0016_book_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_image',
        ),
        migrations.AddField(
            model_name='book',
            name='book_url',
            field=models.TextField(default='null'),
        ),
    ]
