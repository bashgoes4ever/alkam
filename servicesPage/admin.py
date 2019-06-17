from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]

    class Meta:
        model = Service


admin.site.register(Service, ServiceAdmin)


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 3


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceCategory._meta.fields]
    inlines = [ServiceInline]

    class Meta:
        model = ServiceCategory


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
