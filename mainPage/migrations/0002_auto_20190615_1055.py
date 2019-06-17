# Generated by Django 2.2.2 on 2019-06-15 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block4tabs',
            options={'verbose_name': 'Вкладка в 4 блоке', 'verbose_name_plural': 'Вкладки в 4 блоке'},
        ),
        migrations.AlterModelOptions(
            name='mainpageimages',
            options={'verbose_name': 'Изображение во втором блоке', 'verbose_name_plural': 'Изображения во втором блоке'},
        ),
        migrations.AlterModelOptions(
            name='sertificates',
            options={'verbose_name': 'Сертификат', 'verbose_name_plural': 'Сертификаты'},
        ),
        migrations.AddField(
            model_name='sertificates',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]