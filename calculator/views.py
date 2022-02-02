from django.shortcuts import render
from contacts.models import SiteContacts
from .models import Offer


def calculator_view(request):
    contacts = SiteContacts.objects.first()
    offers = Offer.objects.all()
    return render(request, 'calculator.html', locals())
