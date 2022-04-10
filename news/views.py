from django.shortcuts import render
from .models import Article
from contacts.models import SiteContacts


def news_page(request):
    contacts = SiteContacts.objects.first()
    articles = Article.objects.all().order_by('-id')
    return render(request, 'news.html', locals())


def news_single(request, slug):
    contacts = SiteContacts.objects.first()
    article = Article.objects.get(slug=slug)
    return render(request, 'news_single.html', locals())
