from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('service', views.service,name="service"),
    path('product', views.product,name="product"),
    path('price', views.price,name="price"),
    path('team', views.team,name="team"),
    path('testimonial', views.testimonial,name="testimonial"),
    path('blog', views.blog,name="blog"),
    path('detail', views.detail,name="detail"),

    path('login', views.login1,name="login"),
    path('sign', views.sign,name="sign"),
    path('logout', views.logout,name="logout"),


    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart'),


    path('checkout', views.checkout,name="checkout"),
    path('phonefrom', views.phonefrom,name="phonefrom"),
    path('right', views.right,name="right")

    
]