# Generated by Django 2.2.2 on 2019-06-16 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productshop',
            name='pluck',
        ),
    ]
