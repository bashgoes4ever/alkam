from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from shop.models import ProductShop
from django.views.decorators.csrf import csrf_exempt
from contacts.models import SiteContacts
from django.utils.timezone import now
from django.core.mail import send_mail


def basket_page(request):
    contacts = SiteContacts.objects.all()[0]
    session_key = request.session.session_key
    try:
        order = Order.objects.get(user=session_key)
        product_len = len(order.productinbasket_set.all())
    except:
        product_len = 0
    return render(request, 'basket.html', locals())


@csrf_exempt
def add_to_basket(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        order, created = Order.objects.get_or_create(user=session_key)
        quantity = request.POST.get('product_quantity')
        units = request.POST.get('product_units')
        product_params = {
            'order': order,
            'product': ProductShop.objects.get(id=request.POST.get('product_id')),
            'units': units
        }
        product, created = ProductInBasket.objects.get_or_create(**product_params, defaults={'quantity': quantity})
        if not created:
            if units == product.units:
                product.quantity += int(quantity)
                product.save()
            else:
                product_params['quantity'] = quantity
                product_params['units'] = units
                ProductInBasket.objects.create(**product_params)

        product_len = len(Order.objects.get(user=session_key).productinbasket_set.all())
        return JsonResponse({'success': 'true', 'product_len': product_len})


@csrf_exempt
def remove_from_basket(request):
    session_key = request.session.session_key
    order = Order.objects.get(user=session_key)
    ProductInBasket.objects.get(id=request.POST.get('product_id'), order=order).delete()

    order = Order.objects.get(user=session_key)
    product_len = len(Order.objects.get(user=session_key).productinbasket_set.all())
    total_price = order.total_price
    return JsonResponse({
        'success': 'true',
        'product_len': product_len,
        'total_price': total_price
    })


@csrf_exempt
def change_quantity(request):
    session_key = request.session.session_key
    order = Order.objects.get(user=session_key)
    product = ProductInBasket.objects.get(id=request.POST.get('product_id'), order=order)
    product.quantity = int(request.POST.get('product_quantity'))
    product.save()

    order = Order.objects.get(user=session_key)
    product_len = len(Order.objects.get(user=session_key).productinbasket_set.all())
    total_price = order.total_price
    product_total = ProductInBasket.objects.get(id=request.POST.get('product_id'), order=order).total_price
    return JsonResponse({
        'success': 'true',
        'product_len': product_len,
        'total_price': total_price,
        'product_total': product_total
    })


def checkout(request):
    session_key = request.session.session_key
    order = Order.objects.get(user=session_key)
    order.apply_date = now()
    order.user_name = request.POST.get('name')
    order.user_phone = request.POST.get('phone')
    order.user_email = request.POST.get('email')
    order.company_name = request.POST.get('company_name')
    order.user_comment = request.POST.get('text')
    order.delivery = request.POST.get('order_delivery')
    order.save()

    products_data = {}
    products = order.productinbasket_set.all()
    for obj in products:
        products_data['product{}'.format(str(obj.id))] = {
            'name': obj.product.name,
            'price_per_item': obj.price_per_item,
            'quantity': obj.quantity,
            'total_price': obj.total_price
        }
    response_data = {
        'products': products_data,
        'product_len': len(products),
        'order_total_price': order.total_price
    }
    return JsonResponse(response_data)


@csrf_exempt
def send_application(request):
    session_key = request.session.session_key
    order = Order.objects.get(user=session_key)
    products = order.productinbasket_set.all()
    products_string = ''
    for obj in products:
        products_string += '''
            Название товара: {}, 
            Единицы измерения: {}, 
            Количество: {}, 
            Цена за штуку: {}, 
            Общая цена: {}            
        '''.format(obj.product.name, str(obj.units), str(obj.quantity), str(obj.price_per_item), str(obj.total_price))

    message = '''
        Имя: {}, 
        Телефон: {}, 
        Почта: {}, 
        Способ доставки: {}, 
        Название компании: {}, 
        Комментарий: {}, 
        Общая сумма заказа: {}, 
        
        Заказ: {}
        ***
        Более детальную информацию по заказу можно посмотреть в админ панеле на сайте.
    '''.format(order.user_name, order.user_phone, order.user_email, order.delivery, order.company_name,
               order.user_comment, str(order.total_price), products_string)
    send_mail(
        u'Оформление заказа на сайте',
        message,
        'mail@axis-marketing.ru',
        ['alkam.kamensk@yandex.ru'],
        fail_silently=False,
    )
    request.session.flush()
    return JsonResponse({'message': 'applied'})
