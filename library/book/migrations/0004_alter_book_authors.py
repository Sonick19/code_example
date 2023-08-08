# Generated by Django 4.1 on 2023-07-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_remove_author_books'),
        ('book', '0003_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(default=None, to='author.author'),
        ),
    ]