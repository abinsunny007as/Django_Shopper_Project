# Generated by Django 4.2.1 on 2023-06-13 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_cartdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='Product',
            new_name='Brand',
        ),
        migrations.RemoveField(
            model_name='cartdb',
            name='Image',
        ),
    ]
