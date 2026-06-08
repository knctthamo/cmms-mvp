from .services import get_all_assets
from .services import get_active_assets
from django.shortcuts import render, redirect
from .services import create_asset, get_asset_by_id,update_asset,delete_asset
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from accounts.permissions import is_admin

@login_required

def asset_list(request):
    assets = get_all_assets()

    return render(
        request,
        'assets/asset_list.html',
        {
            'assets': assets,
        }
    )

@login_required
def active_asset_list(request):
    assets = get_active_assets()

    return render(
        request,
        'assets/asset_list.html',
        {
            'assets': assets,
            'current_page': 'assets'
        }
    )

@login_required
@user_passes_test(is_admin)
def asset_create(request):

    if request.method == 'POST':

        create_asset(
            asset_code=request.POST['asset_code'],
            name=request.POST['name'],
            installation_date=request.POST['installation_date'],
            status=request.POST['status'],
            criticality=request.POST['criticality']
        )

        return redirect('/assets/')

    return render(
        request,
        'assets/asset_create.html'
    )
# Show details of one asset
@login_required
def asset_detail(request, id):

    # Get asset from service layer
    asset = get_asset_by_id(id)
    work_orders = asset.workorder_set.all()

    # Send asset to HTML template
    return render(
        request,
        'assets/asset_detail.html',
        {
            'asset': asset,
            'work_orders': work_orders
        }
    )


# Edit existing asset
@login_required
def asset_edit(request, id):

    # Load asset for edit page
    asset = get_asset_by_id(id)

    # Save updated data
    if request.method == 'POST':

        update_asset(
            id=id,
            asset_code=request.POST['asset_code'],
            name=request.POST['name'],
            installation_date=request.POST['installation_date'],
            status=request.POST['status'],
            criticality=request.POST['criticality']
        )

        # Redirect to detail page
        return redirect(f'/assets/{id}/')

    # Show pre-filled form
    return render(
        request,
        'assets/asset_edit.html',
        {
            'asset': asset
        }
    )

# Delete asset
@login_required
def asset_delete(request, id):

    # Handle delete confirmation
    if request.method == 'POST':

        delete_asset(id)

        # Go back to asset list
        return redirect('/assets/')

    # Load asset for confirmation screen
    asset = get_asset_by_id(id)

    return render(
        request,
        'assets/asset_delete.html',
        {
            'asset': asset
        }
    )