from django.db import models
from classes import SingletonModel


class SiteContacts(SingletonModel.SingletonModel):
    region = models.CharField(max_length=128, blank=True, null=True, default=u"Свердловская область", verbose_name=u"Область")
    city = models.CharField(max_length=128, blank=True, null=True, default=u"Каменск-Уральский", verbose_name=u"Город")
    street = models.CharField(max_length=128, blank=True, null=True, default=u"ул. Заводская, 9/8", verbose_name=u"Улица, дом")
    email = models.CharField(max_length=128, blank=True, null=True, default=u"plantalkam@mail.ru", verbose_name=u"Email")
    phone1 = models.CharField(max_length=128, blank=True, null=True, default=u"+7 (3439) 399-409", verbose_name=u"Телефон приёмной")
    phone2 = models.CharField(max_length=128, blank=True, null=True, default=u"+7 (3439) 399-409", verbose_name=u"Телефон отдела продаж")
    phone3 = models.CharField(max_length=128, blank=True, null=True, default=u"+7 (3439) 399-409",
                              verbose_name=u"Телефон отдела цветных металлов")
    phone4 = models.CharField(max_length=128, blank=True, null=True, default=u"+7 (3439) 399-409", verbose_name=u"Телефон бухгалтерии")
    map = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Код яндекс карты")

    def __str__(self):
        return u"Контакты"

    class Meta:
        verbose_name = u"Контакты"
        verbose_name_plural = u"Контакты"