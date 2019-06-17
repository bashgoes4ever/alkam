from django.db import models


class ServiceCategory(models.Model):
    title = models.CharField(max_length=128, verbose_name=u"Категория услуг")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Категория услуг"
        verbose_name_plural = u"Категории услуг"


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/services/')
    title = models.CharField(max_length=128, verbose_name=u"Название услуги")

    class Meta:
        verbose_name = u"Услуга"
        verbose_name_plural = u"Услуги"
