# Generated by Django 4.2 on 2023-04-28 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_alter_address_mobileno_alter_student_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookissued',
            old_name='book',
            new_name='books',
        ),
    ]
