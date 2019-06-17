"""mebelmax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.basket_page, name='basket_page'),
    url(r'add_to_basket/', views.add_to_basket, name='add_to_basket'),
    url(r'remove_from_basket/', views.remove_from_basket, name='remove_from_basket'),
    url(r'change_quantity/', views.change_quantity, name='change_quantity'),
    url(r'checkout/', views.checkout, name='checkout'),
    url(r'send_application/', views.send_application, name='send_application'),
]
