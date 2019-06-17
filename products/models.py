from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Вид продукции", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Вид продукции"
        verbose_name_plural = u"Виды продукции"


class ProductCondition(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Состояние поставки", unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Состояние поставки"
        verbose_name_plural = u"Состояния поставки"


class ProductMark(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Сплав", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Марка сплава"
        verbose_name_plural = u"Марки сплава"


class ProductMaterial(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Материал", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Материал"
        verbose_name_plural = u"Материалы"


class ProductStandart(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Стандарт", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Стандарт"
        verbose_name_plural = u"Стандарты"


class Product(models.Model):
    thickness = models.CharField(max_length=50, verbose_name=u"Толщина, мм")
    width = models.CharField(max_length=50, verbose_name=u"Ширина, мм")
    length = models.CharField(max_length=50, verbose_name=u"Длина, мм")
    pluck = models.CharField(max_length=50, verbose_name=u"Плакировка")
    product_type = models.ForeignKey(ProductType, blank=True, null=True, default=None,
                                     on_delete=models.CASCADE, verbose_name=u"Вид продукции")
    product_condition = models.ForeignKey(ProductCondition, blank=True, null=True, default=None,
                                          on_delete=models.CASCADE, verbose_name=u"Состояние поставки")
    product_mark = models.ForeignKey(ProductMark, blank=True, null=True, default=None,
                                     on_delete=models.CASCADE, verbose_name=u"Марка сплава")
    product_material = models.ForeignKey(ProductMaterial, blank=True, null=True, default=None,
                                         on_delete=models.CASCADE, verbose_name=u"Материал")
    product_standart = models.ForeignKey(ProductStandart, blank=True, null=True, default=None,
                                         on_delete=models.CASCADE, verbose_name=u"Стандарт")

    class Meta:
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукты"

