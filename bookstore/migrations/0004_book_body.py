# Generated by Django 4.1.7 on 2023-04-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_alter_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='body',
            field=models.TextField(default='NULL'),
        ),
    ]
