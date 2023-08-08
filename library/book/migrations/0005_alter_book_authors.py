# Generated by Django 4.1 on 2023-07-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_remove_author_books'),
        ('book', '0004_alter_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='author.author'),
        ),
    ]
