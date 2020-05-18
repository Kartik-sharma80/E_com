from django.contrib import admin
from django.urls import path
from home import views



urlpatterns = [
	path('',views.index,name='index'),
	path('register/', views.signup,name='signup'),
	path('login/', views.Login,name='Login'),
	
]
	
    #path('', views.home, name='home'),
   # path("signup",views.Signup.as_view(),name="signup"),
    #path('aftersign/',views.Aftersign.as_view()),
   # path('shop', views.shop, name='shop'),
    #path('contact',views.contact, name='contact'),
    #path('login',views.login,name='login'),
    #path('test',views.test,name='test')'''

''' path('about',views.about, name='about'),
    path('service',views.service, name='service'),
    path('service/IceCreams',views.service, name='service'),
    path('service/Softy',views.service, name='service'),
    path('service/FamilyPack',views.service, name='service'),
    path('contact',views.contact, name='contact'),'''
    
    
