from django.conf import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model


def UserModelString():

    return settings.AUTH_USER_MODEL


def UsernameField():
    return getattr(UserModel(), 'USERNAME_FIELD', 'username')
