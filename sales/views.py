from django.shortcuts import render
from contacts.models import SiteContacts
from .models import Sale


def sales_page(r):
    contacts = SiteContacts.objects.all()[0]
    sales = Sale.objects.all()
    return render(r, 'sales.html', locals())
