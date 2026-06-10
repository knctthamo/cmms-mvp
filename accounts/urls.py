from django.urls import path

from .views import (
    login_view,
    logout_view,
    user_list,
    user_create,
    user_delete,
    user_edit
)

urlpatterns = [

    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'users/',
        user_list,
        name='user_list'
    ),

    path(
        'users/create/',
        user_create,
        name='user_create'
    ),

    path(
        'users/<int:id>/delete/',
        user_delete,
        name='user_delete'
    ),
    
    path(
        'users/<int:id>/edit/',
        user_edit,
        name='user_edit'
    ),
]