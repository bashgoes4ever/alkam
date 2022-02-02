# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from contacts.models import SiteContacts
from .models import Product, ProductMaterial, ProductMark, ProductType, ProductCondition, ProductStandart
from django.core.paginator import Paginator
from django.http import JsonResponse


def products_page(request):
    contacts = SiteContacts.objects.first()
    materials = ProductMaterial.objects.all()
    marks = ProductMark.objects.all()
    types = ProductType.objects.all()
    conditions = ProductCondition.objects.all()

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


def load_products(request):
    contacts = SiteContacts.objects.first()
    if request.method == 'GET':
        if request.user.is_superuser:
            return render(request, 'products-loader.html', locals())
        else:
            return redirect('/')
    else:
        if request.user.is_superuser:
            file = request.FILES['file']
            material, material_created = ProductMaterial.objects.get_or_create(name='алюминий')
            for line in file:
                params = line.decode('cp1251').split('\t')[:-1]
                product_type, created1 = ProductType.objects.get_or_create(name=params[0])
                if params[1] is not '' or params[1] is not '\xa0':
                    state, created2 = ProductCondition.objects.get_or_create(name=params[1])
                mark, created3 = ProductMark.objects.get_or_create(name=params[2])
                standart, created4 = ProductStandart.objects.get_or_create(name=params[3])
                try:
                    thickness = params[4]
                except:
                    thickness = ''
                try:
                    width = params[5]
                except:
                    width = ''
                try:
                    lenght = params[6]
                except:
                    lenght = ''
                try:
                    pluck = params[7]
                except:
                    pluck = ''
                product = Product.objects.create(thickness=thickness, width=width, length=lenght,
                                                 pluck=pluck, product_type=product_type, product_condition=state,
                                                 product_mark=mark, product_standart=standart, product_material=material)
            return JsonResponse({'success': 'true'})
        else:
            return JsonResponse({'success': 'false'})
