from django.urls import path
from cars import views as carsView

urlpatterns = [
    path('list', carsView.list_car),
    path('store', carsView.store_car),
    path('<int:id>', carsView.detail_car),
    path('<int:id>/update', carsView.update_car),
    path('<int:id>/delete', carsView.delete_car),
]