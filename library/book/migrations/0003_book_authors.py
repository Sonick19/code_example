# Generated by Django 4.1 on 2023-07-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_remove_author_books'),
        ('book', '0002_book_count_book_description_book_name_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='author.author'),
        ),
    ]
