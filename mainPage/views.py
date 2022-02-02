from django.shortcuts import render
from .models import *
from contacts.models import SiteContacts
from news.models import Article
from django.http import JsonResponse
from django.core.mail import send_mail


def main(request):
    slider_images = MainPageImages.objects.all()
    tabs = Block4Tabs.objects.all()
    sertificates = Sertificates.objects.order_by("-date")[:4]
    news = Article.objects.all()[:2]
    contacts = SiteContacts.objects.first()
    return render(request, 'index.html', locals())


def send_form(request):
    if request.POST.get('polit') is "1":
        message = ''
        if request.POST.get('type'):
            message += '\t'+request.POST.get('type')
        if request.POST.get('name'):
            message += '''
            Имя: {}'''.format(request.POST.get('name'))
        if request.POST.get('phone'):
            message += '''
            Телефон: {}'''.format(request.POST.get('phone'))
        if request.POST.get('email'):
            message += '''
            email: {}'''.format(request.POST.get('email'))
        if request.POST.get('text'):
            message += '''
            Комментарий: {}'''.format(request.POST.get('text'))
        if request.POST.get('mark'):
            message += '''
            Марка: {}'''.format(request.POST.get('mark'))
        if request.POST.get('business'):
            message += '''
            Род деятельности: {}'''.format(request.POST.get('business'))
        if request.POST.get('company_name'):
            message += '''
            Название компании: {}'''.format(request.POST.get('company_name'))

        send_mail(
            request.POST.get('type'),
            message,
            'mail@axis-marketing.ru',
            ['alkam.kamensk@yandex.ru'],
            fail_silently=False,
        )
        return JsonResponse({'message': 'applied'})
    else:
        return JsonResponse({'message': 'not applied'})
