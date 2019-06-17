from django.contrib import admin
from .models import *


class EquipmentImagesInline(admin.TabularInline):
    model = EquipmentImages
    extra = 3


class EquipmentListObjectInline(admin.TabularInline):
    model = EquipmentListObject
    extra = 3


class EquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipments._meta.fields]
    inlines = [EquipmentImagesInline, EquipmentListObjectInline]

    class Meta:
        model = Equipments


admin.site.register(Equipments, EquipmentAdmin)
