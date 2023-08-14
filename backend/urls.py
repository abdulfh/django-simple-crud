"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from cars import views as carsView
from orders import views as ordersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/list', carsView.list_car),
    path('cars/store', carsView.store_car),
    path('cars/<int:id>', carsView.detail_car),
    path('cars/<int:id>/update', carsView.update_car),
    path('cars/<int:id>/delete', carsView.delete_car),
    
    path('orders/list', ordersView.list_order),
    path('orders/store', ordersView.store_order),
    path('orders/<int:id>', ordersView.detail_order),
    path('orders/<int:id>/update', ordersView.update_order),
    path('orders/<int:id>/delete', ordersView.delete_order)
]