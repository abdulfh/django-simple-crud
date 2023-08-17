from django.urls import path
from orders import views as ordersView

app_name = 'orders'
urlpatterns = [
    path('list', ordersView.list_order),
    path('store', ordersView.store_order),
    path('<int:id>', ordersView.detail_order),
    path('<int:id>/update', ordersView.update_order),
    path('<int:id>/delete', ordersView.delete_order)
]