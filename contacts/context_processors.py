from .models import SiteContacts

def settings(request):
    return {'settings': SiteContacts.load()}