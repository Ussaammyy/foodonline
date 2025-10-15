from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.Home,name="home"),
    path("about/",views.about,name="about"),
    path("Cart/",views.cart,name="cart"),
]