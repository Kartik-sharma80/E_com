from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('contact',views.contact, name='contact'),
]
''' path('about',views.about, name='about'),
    path('service',views.service, name='service'),
    path('service/IceCreams',views.service, name='service'),
    path('service/Softy',views.service, name='service'),
    path('service/FamilyPack',views.service, name='service'),
    path('contact',views.contact, name='contact'),'''
    