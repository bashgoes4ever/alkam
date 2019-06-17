from django.contrib import admin
from .models import *

admin.site.register(ProductShopType)
admin.site.register(ProductShopMark)
admin.site.register(ProductShopMaterial)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductShop._meta.fields]

    class Meta:
        model = ProductShop


admin.site.register(ProductShop, ProductAdmin)
