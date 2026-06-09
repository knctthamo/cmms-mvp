from django.urls import path
from .views import work_order_list,work_order_create,work_order_detail,work_order_edit,work_order_delete, my_work_orders,update_work_order_status

urlpatterns = [
    path('', work_order_list, name='work_order_list'),
    path('create/',work_order_create,name='work_order_create'),
    path('<int:id>/update-status/',update_work_order_status,name='update_work_order_status'),
    path('<int:id>/',work_order_detail,name='work_order_detail'),
    path('<int:id>/edit/', work_order_edit,name='work_order_edit'),
    path('<int:id>/delete/',work_order_delete,name='work_order_delete'),
    path('my-work-orders/',my_work_orders,name='my_work_orders'),
]