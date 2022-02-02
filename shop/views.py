from django.shortcuts import render
from contacts.models import SiteContacts
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from basket.models import Order
from django.urls import reverse


def get_products_paginated(request):
    OBJECTS_PER_PAGE = 10
    # фильтр продукции
    filters = {}
    if request.POST.get('materials') is not 'all':
        try:
            filters['product_material_id'] = ProductShopMaterial.objects.get(name__exact=request.POST.get('materials')).id
        except:
            pass
    if request.POST.get('marks') is not 'all':
        try:
            filters['product_mark_id'] = ProductShopMark.objects.get(name__exact=request.POST.get('marks')).id
        except:
            pass
    if request.POST.get('thickness') is not 'all':
        try:
            filters['thickness'] = float(request.POST.get('thickness'))
        except:
            pass
    if request.POST.get('is_sale') == 'sale':
        try:
            filters['is_sale'] = True
        except:
            pass
    else:
        filters['is_sale'] = False

    if filters:
        products = ProductShop.objects.filter(**filters)
    else:
        products = ProductShop.objects.all()

    # соритровка продукции
    if request.POST.get('sort_name') == 'thickness':
        if request.POST.get('sort') == 'up':
            products = products.order_by('thickness')
        else:
            products = products.order_by('-thickness')
    elif request.POST.get('sort_name') == 'price_per_kilo':
        if request.POST.get('sort') == 'up':
            products = products.order_by('price_per_kilo')
        else:
            products = products.order_by('-price_per_kilo')

    paginator = Paginator(products, OBJECTS_PER_PAGE)

    if request.method == 'GET':
        page = paginator.get_page(request.GET.get('page', 1))
    else:
        page = paginator.get_page(request.POST.get('page', 1))

    is_paginated = page.has_other_pages()

    if page.has_previous():
        page_prev = page.previous_page_number()
    else:
        page_prev = ''

    if page.has_next():
        page_next = page.next_page_number()
    else:
        page_next = ''

    return products, page, is_paginated, page_prev, page_next


@csrf_exempt
def shop_page(request):
    session_key = request.session.session_key
    try:
        product_len = len(Order.objects.get(user=session_key).productinbasket_set.all())
    except:
        product_len = 0
    if not session_key:
        request.session.cycle_key()

    if request.method == 'GET':
        contacts = SiteContacts.objects.all()[0]
        materials = ProductShopMaterial.objects.all()
        marks = ProductShopMark.objects.all()
        thickness = set(ProductShop.objects.all().values_list('thickness', flat=True).order_by('thickness'))
        products, page, is_paginated, page_prev, page_next = get_products_paginated(request)
        return render(request, 'shop.html', locals())
    else:
        products, page, is_paginated, page_prev, page_next = get_products_paginated(request)
        products_data = {}

        for obj in page.object_list:
            products_data['product'+str(obj.id)] = {
                'id': obj.id,
                'name': obj.name,
                'price': obj.price_per_kilo,
            }

        if not page_prev:
            pagination = '''
            <li class="nav-button-prev page-item disabled">
                <a class="page-link" href="{}">Назад</a>
            </li>
            '''.format(page_prev)
        else:
            pagination = '''
            <li class="nav-button-prev page-item">
                <a class="page-link" href="{}">Назад</a>
            </li>
            '''.format(page_prev)

        for n in page.paginator.page_range:
            if n > page.number - 3 and n < page.number + 3:
                if page.number == n:
                    pagination = pagination + '''
                        <li class="page-item active">
                            <a class="page-link" href="{}">{}</a>
                        </li>
                    '''.format(n, n)
                else:
                    pagination = pagination + '''
                        <li class="page-item">
                            <a class="page-link" href="{}">{}</a>
                        </li>
                    '''.format(n, n)

        if not page_next:
            pagination = pagination + '''
            <li class="nav-button-next page-item disabled">
                <a class="page-link" href="{}">Далее</a>
            </li>
            '''.format(page_next)
        else:
            pagination = pagination + '''
            <li class="nav-button-next page-item">
                <a class="page-link" href="{}">Далее</a>
            </li>
            '''.format(page_next)

        response_data = {
            'products': products_data,
            'add_cart_url': reverse('add_to_basket'),
            'is_paginated': is_paginated,
            'page_prev': page_prev,
            'page_next': page_next,
            'pagination': pagination,
            'current_page': int(request.POST.get('page', 1))
        }
        return JsonResponse(response_data)


@csrf_exempt
def get_price(request):
    price = ProductShop.objects.get(id=request.POST.get('id')).price_per_unit if request.POST.get('units') == 'шт' else \
            ProductShop.objects.get(id=request.POST.get('id')).price_per_kilo
    return HttpResponse(price)
