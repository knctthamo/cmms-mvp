from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test
)

from django.contrib.auth.models import Group

from .services import (
    get_all_users,
    create_user,
    get_user_by_id,
    delete_user,
    update_user
)

from .permissions import is_admin


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('/dashboard/')

    return render(
        request,
        'accounts/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('/login/')


@login_required
@user_passes_test(is_admin)
def user_list(request):

    users = get_all_users()

    return render(
        request,
        'accounts/user_list.html',
        {
            'users': users,
            'current_page': 'users',
        }
    )


@login_required
@user_passes_test(is_admin)
def user_create(request):

    if request.method == 'POST':

        create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            role=request.POST['role'],
            phone_number=request.POST['phone_number']
        )

        return redirect('/users/')

    groups = Group.objects.all()

    return render(
        request,
        'accounts/user_create.html',
        {
            'groups': groups,
            'current_page': 'users',
        }
    )


@login_required
@user_passes_test(is_admin)
def user_edit(request, id):

    user = get_user_by_id(id)

    if request.method == 'POST':

        update_user(
            id=id,
            username=request.POST['username'],
            role=request.POST['role'],
            phone_number=request.POST['phone_number']
        )

        return redirect('/users/')

    groups = Group.objects.all()

    return render(
        request,
        'accounts/user_edit.html',
        {
            'user_obj': user,
            'groups': groups,
            'current_page': 'users',
        }
    )

@login_required
@user_passes_test(is_admin)
def user_delete(request, id):

    if request.method == 'POST':

        delete_user(id)

        return redirect('/users/')

    user = get_user_by_id(id)

    return render(
        request,
        'accounts/user_delete.html',
        {
            'user_obj': user,
            'current_page': 'users',
        }
    )