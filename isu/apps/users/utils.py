from rest_framework.authtoken.models import Token


def get_token_func(user):
    token = Token.objects.get_or_create(user=user)[0]
    return token.key

