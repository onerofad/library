# Generated by Django 4.2 on 2023-05-03 16:44

from django.db import migrations, models
import django.db.models.deletion
import library_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0011_rename_book_bookissued_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookissued',
            name='books',
        ),
        migrations.AddField(
            model_name='bookissued',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='library_app.book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(unique=True, upload_to=library_app.models.book_upload_to),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]