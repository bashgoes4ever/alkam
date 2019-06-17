from django.contrib import admin
from .models import *

admin.site.register(ProductInBasket)


class ProductInBasketInline(admin.TabularInline):
    model = ProductInBasket
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInBasketInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)