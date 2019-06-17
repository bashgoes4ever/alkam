from django.shortcuts import render
from contacts.models import SiteContacts


def calculator_view(request):
    contacts = SiteContacts.objects.first()
    return render(request, 'calculator.html', locals())
