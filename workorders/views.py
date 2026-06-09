from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from assets.models import Asset

from .services import (
    get_all_work_orders,
    create_work_order,
    get_work_order_by_id,
    update_work_order,
    delete_work_order,
    get_technicians
)

from accounts.permissions import is_admin_or_manager


# Show all work orders
@login_required
def work_order_list(request):

    work_orders = get_all_work_orders()

    return render(
        request,
        'workorders/work_order_list.html',
        {
            'work_orders': work_orders,
            'current_page': 'workorders',
        }
    )


# Create work order
@login_required
@user_passes_test(is_admin_or_manager)
def work_order_create(request):

    if request.method == 'POST':

        create_work_order(
            title=request.POST['title'],
            description=request.POST['description'],
            asset_id=request.POST['asset'],
            assigned_to_id=request.POST['assigned_to'],
            due_date=request.POST['due_date']
        )

        return redirect('/workorders/')

    assets = Asset.objects.all()

    technicians = get_technicians()

    return render(
        request,
        'workorders/work_order_create.html',
        {
            'assets': assets,
            'technicians': technicians,
            'current_page': 'workorders',
        }
    )


# Show work order details
@login_required
def work_order_detail(request, id):

    work_order = get_work_order_by_id(id)

    return render(
        request,
        'workorders/work_order_detail.html',
        {
            'work_order': work_order,
            'current_page': 'workorders',
        }
    )


# Edit work order
@login_required
@user_passes_test(is_admin_or_manager)
def work_order_edit(request, id):

    if request.method == 'POST':

        update_work_order(
            id=id,
            title=request.POST['title'],
            description=request.POST['description'],
            asset_id=request.POST['asset'],
            assigned_to_id=request.POST['assigned_to'],
            due_date=request.POST['due_date'],
            status=request.POST['status']
        )

        return redirect(f'/workorders/{id}/')

    work_order = get_work_order_by_id(id)

    assets = Asset.objects.all()

    technicians = get_technicians()

    return render(
        request,
        'workorders/work_order_edit.html',
        {
            'work_order': work_order,
            'assets': assets,
            'technicians': technicians,
            'current_page': 'workorders',
        }
    )


# Delete work order
@login_required
@user_passes_test(is_admin_or_manager)
def work_order_delete(request, id):

    if request.method == 'POST':

        delete_work_order(id)

        return redirect('/workorders/')

    work_order = get_work_order_by_id(id)

    return render(
        request,
        'workorders/work_order_delete.html',
        {
            'work_order': work_order,
            'current_page': 'workorders',
        }
    )