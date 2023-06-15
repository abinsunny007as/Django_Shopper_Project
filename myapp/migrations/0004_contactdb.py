# Generated by Django 4.2.1 on 2023-05-23 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_productdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(blank=True, max_length=50, null=True)),
                ('Lname', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Subject', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
