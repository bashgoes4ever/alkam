from django.contrib import admin
from .models import SiteContacts


class SiteContactsAdmin(admin.ModelAdmin):
    list_display = ('contacts_admin_name',)

    def contacts_admin_name(self):
        return 'Контакты'


admin.site.register(SiteContacts)
