from django.contrib.auth.models import User, Group


def get_all_users():

    return User.objects.all()


def create_user(
    username,
    password,
    role,
    phone_number
):

    user = User.objects.create_user(
        username=username,
        password=password
    )

    group = Group.objects.get(
        name=role
    )

    user.groups.add(group)

    user.userprofile.phone_number = phone_number
    user.userprofile.save()

    return user

def get_user_by_id(id):

    return User.objects.get(id=id)


def delete_user(id):

    user = User.objects.get(id=id)

    user.delete()