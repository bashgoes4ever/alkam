from django.db import models
from django.utils.timezone import now
from shop.models import ProductShop
from django.db.models.signals import post_save, post_delete
from functools import wraps


class Order(models.Model):
    user = models.CharField(max_length=128, blank=False, verbose_name=u"Пользователь")  # session key
    start_date = models.DateTimeField(default=now, editable=False, verbose_name=u"Первый товар положен в корзину")
    apply_date = models.DateTimeField(default=None, null=True, blank=True, verbose_name=u"Оформление заказа")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=u"Общая стоимость")
    user_name = models.CharField(max_length=128, blank=True, verbose_name=u"ФИО")
    user_email = models.EmailField(blank=True, verbose_name=u"Email")
    user_phone = models.CharField(max_length=128, blank=True, verbose_name=u"Номер телефона")
    company_name = models.CharField(max_length=128, blank=True, verbose_name=u"Название компании")
    user_comment = models.TextField(max_length=500, blank=True, verbose_name=u"Комментарий")
    delivery = models.TextField(max_length=256, blank=True, verbose_name=u"Доставка")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInBasket(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None,
                                     on_delete=models.CASCADE, verbose_name=u"Заказ")
    product = models.ForeignKey(ProductShop, blank=True, null=True, default=None,
                                     on_delete=models.CASCADE, verbose_name=u"Товар")
    quantity = models.IntegerField(default=1, verbose_name=u"Количество")
    units = models.CharField(max_length=10, default='кг', verbose_name=u"Единица измерения")
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=u"Цена за ед.")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=u"Общая сумма")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        if self.units == 'кг':
            price_per_item = self.product.price_per_kilo
        else:
            price_per_item = self.product.price_per_unit
        self.price_per_item = price_per_item
        self.total_price = int(self.quantity) * price_per_item

        all_products = Order.objects.get(id=self.order.id).productinbasket_set.all()
        order_total_price = 0
        for item in all_products:
            order_total_price += item.total_price

        super(ProductInBasket, self).save(*args, **kwargs)


def disable_for_loaddata(signal_handler):
    """
    Decorator that turns off signal handlers when loading fixture data.
    """
    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        if kwargs['raw']:
            return
        signal_handler(*args, **kwargs)
    return wrapper


@disable_for_loaddata
def product_in_basket_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products = Order.objects.get(id=order.id).productinbasket_set.all()
    order_total_price = 0
    for item in all_products:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


def product_in_basket_post_delete(sender, instance, **kwargs):
    order = instance.order
    all_products = Order.objects.get(id=order.id).productinbasket_set.all()
    order_total_price = 0
    for item in all_products:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_basket_post_save, sender=ProductInBasket)
post_delete.connect(product_in_basket_post_delete, sender=ProductInBasket)
