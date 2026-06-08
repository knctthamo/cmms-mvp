from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.groups.filter(name='Admin').exists()


def is_manager(user):
    return user.groups.filter(name='Manager').exists()


def is_technician(user):
    return user.groups.filter(name='Technician').exists()