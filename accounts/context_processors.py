from accounts.permissions import (
    is_admin,
    is_manager,
    is_technician,
    is_admin_or_manager
)


def user_roles(request):
    if not request.user.is_authenticated:
        return {}

    return {
        'is_admin': is_admin(request.user),
        'is_manager': is_manager(request.user),
        'is_technician': is_technician(request.user),
        'is_admin_or_manager': is_admin_or_manager(request.user),
    }