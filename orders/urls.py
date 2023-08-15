from django.urls import path
from orders import views as ordersView

urlpatterns = [
    path('orders/list', ordersView.list_order),
    path('orders/store', ordersView.store_order),
    path('orders/<int:id>', ordersView.detail_order),
    path('orders/<int:id>/update', ordersView.update_order),
    path('orders/<int:id>/delete', ordersView.delete_order)
]