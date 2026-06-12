from django.contrib.auth.models import User, Group


def get_all_users():

    return User.objects.all()


def create_user(
    username,
    password,
    role,
    phone_number,
    telegram_chat_id
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

    user.userprofile.telegram_chat_id = (
        telegram_chat_id
    )

    user.userprofile.save()

    return user

def get_user_by_id(id):

    return User.objects.get(id=id)


def delete_user(id):

    user = User.objects.get(id=id)

    user.delete()

def update_user(
    id,
    username,
    role,
    phone_number,
    telegram_chat_id
):

    user = User.objects.get(id=id)

    user.username = username
    user.save()

    user.groups.clear()

    group = Group.objects.get(
        name=role
    )

    user.groups.add(group)

    user.userprofile.phone_number = (
        phone_number
    )

    user.userprofile.telegram_chat_id = (
    telegram_chat_id
    )

    user.userprofile.save()

    return user