from django.contrib import admin
from django.urls import path
from expectprice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calc, name='home'),
    path('calc/', views.calc, name='calc'),
]
