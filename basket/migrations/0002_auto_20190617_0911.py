# Generated by Django 2.2.2 on 2019-06-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_type',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, max_length=128, verbose_name='Доставки'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена за ед.'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая сумма'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='units',
            field=models.CharField(default='кг', max_length=10, verbose_name='Единица измерения'),
        ),
    ]
