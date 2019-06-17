from django.db import models


class ProductShopType(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Вид продукции", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Вид продукции"
        verbose_name_plural = u"Виды продукции"


class ProductShopMark(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Сплав", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Марка сплава"
        verbose_name_plural = u"Марки сплава"


class ProductShopMaterial(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Материал", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Материал"
        verbose_name_plural = u"Материалы"


class ProductShop(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Название")
    thickness = models.FloatField(verbose_name=u"Толщина, мм")
    width = models.CharField(max_length=50, verbose_name=u"Ширина, мм")
    length = models.CharField(max_length=50, verbose_name=u"Длина, мм")
    product_type = models.ForeignKey(ProductShopType, blank=True, null=True, default=None,
                                     on_delete=models.CASCADE, verbose_name=u"Вид продукции")
    product_mark = models.ForeignKey(ProductShopMark, blank=True, null=True, default=None,
                                     on_delete=models.CASCADE, verbose_name=u"Марка сплава")
    product_material = models.ForeignKey(ProductShopMaterial, blank=True, null=True, default=None,
                                         on_delete=models.CASCADE, verbose_name=u"Материал")
    price_per_kilo = models.IntegerField(verbose_name=u"Цена за кг")
    price_per_unit = models.IntegerField(verbose_name=u"Цена за штуку")
    is_sale = models.BooleanField(default=False, verbose_name=u"Товар по распродаже")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукты"

