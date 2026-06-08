from django.shortcuts import render

from assets.models import Asset
from workorders.models import WorkOrder
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    total_assets = Asset.objects.count()

    active_assets = Asset.objects.filter(
        status='ACTIVE'
    ).count()

    inactive_assets = Asset.objects.filter(
        status='INACTIVE'
    ).count()

    total_work_orders = WorkOrder.objects.count()

    open_work_orders = WorkOrder.objects.filter(
        status='OPEN'
    ).count()

    completed_work_orders = WorkOrder.objects.filter(
        status='COMPLETED'
    ).count()

    recent_work_orders = WorkOrder.objects.order_by(
        '-id'
    )[:5]

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'total_assets': total_assets,
            'active_assets': active_assets,
            'inactive_assets': inactive_assets,
            'total_work_orders': total_work_orders,
            'open_work_orders': open_work_orders,
            'completed_work_orders': completed_work_orders,
            'recent_work_orders': recent_work_orders,
            "current_page": "dashboard",
            'groups': request.user.groups.all(),


        }
    )
