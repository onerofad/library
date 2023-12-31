# Generated by Django 4.2 on 2023-04-17 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_isbn10',
            field=models.CharField(default='Null', max_length=400),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_isbn13',
            field=models.CharField(default='Null', max_length=400),
        ),
        migrations.CreateModel(
            name='BookIssued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateissued', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.student')),
            ],
        ),
    ]
