from django.shortcuts import render
from contacts.models import SiteContacts
from .models import Product, ProductMaterial, ProductMark, ProductType
from django.core.paginator import Paginator


def products_page(request):
    contacts = SiteContacts.objects.first()
    materials = ProductMaterial.objects.all()
    marks = ProductMark.objects.all()
    types = ProductType.objects.all()

    filters = {}
    query = ''
    if request.GET.get('material'):
        try:
            filters['product_material_id'] = ProductMaterial.objects.get(name__iexact=request.GET.get('material')).id
            query = query+'&material='+request.GET.get('material')
        except:
            pass
    if request.GET.get('mark'):
        try:
            filters['product_mark_id'] = ProductMark.objects.get(name__iexact=request.GET.get('mark')).id
            query = query+'&mark='+request.GET.get('mark')
        except:
            pass
    if request.GET.get('type'):
        try:
            filters['product_type_id'] = ProductType.objects.get(name__iexact=request.GET.get('type')).id
            query = query + '&type=' + request.GET.get('type')
        except:
            pass

    if filters:
        products = Product.objects.filter(**filters)
    else:
        products = Product.objects.all()



    paginator = Paginator(products, 10)
    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        page_prev = '?page={}'.format(page.previous_page_number())
    else:
        page_prev = ''

    if page.has_next():
        page_next = '?page={}'.format(page.next_page_number())
    else:
        page_next = ''

    return render(request, 'products.html', locals())
