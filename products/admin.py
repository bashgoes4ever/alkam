from django.contrib import admin
from .models import *

admin.site.register(ProductType)
admin.site.register(ProductCondition)
admin.site.register(ProductMark)
admin.site.register(ProductMaterial)
admin.site.register(ProductStandart)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
