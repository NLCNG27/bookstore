# Generated by Django 4.1.7 on 2023-04-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_remove_book_body_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(),
        ),
    ]
