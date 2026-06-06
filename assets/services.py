from .models import Asset


def get_all_assets():
    return Asset.objects.all()

def get_active_assets():
    return Asset.objects.filter(status='ACTIVE')

def create_asset(
    asset_code,
    name,
    installation_date,
    status,
    criticality
):
    return Asset.objects.create(
        asset_code=asset_code,
        name=name,
        installation_date=installation_date,
        status=status,
        criticality=criticality
    )

# Get a single asset using primary key
def get_asset_by_id(id):

    # Fetch exactly one asset
    return Asset.objects.get(id=id)

# Update existing asset
def update_asset(
    id,
    asset_code,
    name,
    installation_date,
    status,
    criticality
):

    # Fetch existing asset
    asset = Asset.objects.get(id=id)

    # Update fields
    asset.asset_code = asset_code
    asset.name = name
    asset.installation_date = installation_date
    asset.status = status
    asset.criticality = criticality

    # Save changes to database
    asset.save()

    return asset

# Delete existing asset
def delete_asset(id):

    # Get asset
    asset = Asset.objects.get(id=id)

    # Delete asset
    asset.delete()