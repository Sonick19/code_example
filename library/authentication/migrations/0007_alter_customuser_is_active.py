# Generated by Django 4.1 on 2023-07-03 19:10


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_customuser_is_staff_customuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
