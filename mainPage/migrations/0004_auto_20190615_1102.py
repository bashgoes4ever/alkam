# Generated by Django 2.2.2 on 2019-06-15 08:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0003_auto_20190615_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sertificates',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
