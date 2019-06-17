from django.shortcuts import render
from contacts.models import SiteContacts
from .models import Equipments


def about_page(request):
    contacts = SiteContacts.objects.first()
    equipments = Equipments.objects.all()
    return render(request, 'about.html', locals())