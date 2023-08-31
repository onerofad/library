# Generated by Django 4.2 on 2023-04-26 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0009_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='mobileno',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.address', to_field='mobileno'),
        ),
    ]
