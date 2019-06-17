from django.shortcuts import render
from .models import ServiceCategory
from contacts.models import SiteContacts


def services_page(request):
    categories = ServiceCategory.objects.all()
    contacts = SiteContacts.objects.first()
    return render(request, 'services.html', locals())
