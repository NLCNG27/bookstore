# Generated by Django 4.1.7 on 2023-04-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='body',
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(default='XXXX', max_length=4),
        ),
    ]