# Generated by Django 3.0.2 on 2022-02-09 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]