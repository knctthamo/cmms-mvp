from django.urls import path
from .views import asset_list, active_asset_list,asset_create,asset_detail,asset_edit,asset_delete

urlpatterns = [
    path('', asset_list, name='asset_list'),
    path('active', active_asset_list, name='asset_list'),
    path('create/', asset_create, name='asset_create'),
    path('<int:id>/', asset_detail, name='asset_detail'),
    path('<int:id>/edit/', asset_edit, name='asset_edit'),
    path('<int:id>/delete/', asset_delete, name='asset_delete'),
]