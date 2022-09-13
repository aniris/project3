from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('calc/', include(('expectprice.urls', 'calc'), namespace='expectprice')),
]
