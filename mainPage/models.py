from django.db import models
from tinymce.models import HTMLField
from django.utils.timezone import now


class MainPageImages(models.Model):
    image = models.ImageField(upload_to='static/img/block2/slider/', verbose_name=u"Изображение")

    class Meta:
        verbose_name = u"Изображение во втором блоке"
        verbose_name_plural = u"Изображения во втором блоке"


class Block4Tabs(models.Model):
    image = models.ImageField(upload_to='static/img/block4/', verbose_name=u"Изображение")
    tab_text = models.CharField(max_length=128, verbose_name=u"Заголовок справа")
    title = models.CharField(max_length=128, verbose_name=u"Заголовок")
    text = HTMLField(verbose_name=u"Текст")

    class Meta:
        verbose_name = u"Вкладка в 4 блоке"
        verbose_name_plural = u"Вкладки в 4 блоке"


class Sertificates(models.Model):
    image = models.ImageField(upload_to='static/img/block5/', verbose_name=u"Изображение")
    date = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name = u"Сертификат"
        verbose_name_plural = u"Сертификаты"
