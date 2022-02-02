"""webApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('mainPage.urls')),
    url(r'about/', include('aboutPage.urls')),
    url(r'news/', include('news.urls')),
    url(r'services/', include('servicesPage.urls')),
    url(r'products/', include('products.urls')),
    url(r'shop/', include('shop.urls')),
    url(r'cart/', include('basket.urls')),
    url(r'offers/', include('calculator.urls')),
    url(r'sales/', include('sales.urls')),
    url(r'^tinymce/', include('tinymce.urls'))
]
