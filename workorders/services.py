from django.contrib.auth.models import User

from .models import WorkOrder
from assets.models import Asset


# Generate next work order number
def generate_work_order_number():

    last_work_order = WorkOrder.objects.order_by('-id').first()

    if last_work_order:
        return f"WO-{last_work_order.id + 1:04d}"

    return "WO-0001"


# Get all work orders
def get_all_work_orders():

    return WorkOrder.objects.all()


# Get technicians
def get_technicians():

    return User.objects.filter(
        groups__name='Technician'
    )


# Create work order
def create_work_order(
    title,
    description,
    asset_id,
    assigned_to_id,
    due_date
):

    work_order_number = generate_work_order_number()

    asset = Asset.objects.get(id=asset_id)

    assigned_to = User.objects.get(
        id=assigned_to_id
    )

    work_order = WorkOrder.objects.create(
        work_order_number=work_order_number,
        title=title,
        description=description,
        asset=asset,
        assigned_to=assigned_to,
        due_date=due_date
    )

    print("\n========================")

    print(
        f"WhatsApp To: "
        f"{assigned_to.userprofile.phone_number}"
    )

    print(
        f"""
    New Work Order Assigned

    WO Number:
    {work_order.work_order_number}

    Title:
    {work_order.title}

    Asset:
    {asset.asset_code}

    Due Date:
    {work_order.due_date}

    Please login to CMMS and update the status.
    """
    )

    print("========================\n")

    return work_order

# Get work order by id
def get_work_order_by_id(id):

    return WorkOrder.objects.get(id=id)


# Update work order
def update_work_order(
    id,
    title,
    description,
    asset_id,
    assigned_to_id,
    due_date,
    status
):

    work_order = WorkOrder.objects.get(id=id)

    asset = Asset.objects.get(id=asset_id)

    assigned_to = User.objects.get(
        id=assigned_to_id
    )

    work_order.title = title
    work_order.description = description
    work_order.asset = asset
    work_order.assigned_to = assigned_to
    work_order.due_date = due_date
    work_order.status = status

    work_order.save()

    return work_order


# Delete work order
def delete_work_order(id):

    work_order = WorkOrder.objects.get(id=id)

    work_order.delete()

def get_work_orders_for_technician(user):

    return WorkOrder.objects.filter(
        assigned_to=user
    )

def update_status(
    id,
    status
):

    work_order = WorkOrder.objects.get(
        id=id
    )

    work_order.status = status

    work_order.save()

    return work_order