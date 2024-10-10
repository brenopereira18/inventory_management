from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from . import views

def home_view(request):
    return render(
        request,
        'base.html',
    )

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('', include('brands.urls')),
    path('', include('categories.urls')),    
    path('', include('suppliers.urls')), 
    path('', include('inflows.urls')), 
    path('', include('outflows.urls')), 
    path('', include('products.urls')), 
]
