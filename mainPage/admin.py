from django.contrib import admin
from .models import *


class MainPageImagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MainPageImages._meta.fields]

    class Meta:
        model = MainPageImages


admin.site.register(MainPageImages, MainPageImagesAdmin)


class Block4TabsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Block4Tabs._meta.fields]

    class Meta:
        model = Block4Tabs


admin.site.register(Block4Tabs, Block4TabsAdmin)


class SertificatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sertificates._meta.fields]
    exclude = ('date',)

    class Meta:
        model = Sertificates


admin.site.register(Sertificates, SertificatesAdmin)