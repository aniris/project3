from django.contrib import admin
from django.urls import path
from expectprice import views

app_name = 'expectprice'

urlpatterns = [
    path('calc/', views.calc, name='calc'),
]
