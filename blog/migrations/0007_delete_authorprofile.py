# Generated by Django 3.2.6 on 2022-07-18 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_authorprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthorProfile',
        ),
    ]
