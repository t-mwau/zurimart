
from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
    path('index/', views.index),
    path('services/', views.services),
    path('products/', views.products),
]
