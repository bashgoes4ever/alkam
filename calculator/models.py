from django.db import models
from tinymce.models import HTMLField


class Offer(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"Заголовок")
    text = HTMLField(verbose_name=u"Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Предложение сотрудничества"
        verbose_name_plural = u"Предложения сотрудничества"
