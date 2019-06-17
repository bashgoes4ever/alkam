from django.db import models
from tinymce.models import HTMLField


class Equipments(models.Model):
    tab = models.CharField(max_length=128, verbose_name=u"Название вкладки")
    title = HTMLField(verbose_name=u"Заголовок")

    class Meta:
        verbose_name = u"Оборудование"
        verbose_name_plural = u"Оборудование"


class EquipmentImages(models.Model):
    equipment = models.ForeignKey(Equipments, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/equipments/')

    class Meta:
        verbose_name = u"Фото оборудования"
        verbose_name_plural = u"Фото оборудования"


class EquipmentListObject(models.Model):
    equipment = models.ForeignKey(Equipments, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = models.CharField(max_length=128, verbose_name=u"Название оборудования")

    class Meta:
        verbose_name = u"Название оборудования"
        verbose_name_plural = u"Названия оборудования"


