from apps.users.models import CompanyInfo, User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse

from apps.users.utils import get_token_func
from apps.category.models import Category
from .tasks import send_activate_link


class LoginService:
    @staticmethod
    def login_user(data):
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            data = {
                "token": get_token_func(user)
            }
            return data
    

class RegistrationService:
    @staticmethod
    def user_registration(data):
        is_company = data.get("is_company")
        if is_company:
            company_name = data.pop("company_name")
            description = data.pop("description")
            category = Category.objects.create(type_of=data.pop("category"))
        user = get_user_model().objects.create(**data)
        if is_company:
            CompanyInfo.objects.create(
                name=company_name,
                description=description,
                category=category,
                user=user
            )
        return user
    

class ActivationService:
    @staticmethod
    def send_activation_mail(request, user):
        uidb64 = urlsafe_base64_encode(force_bytes(user.id))
        token = get_token_func(user)
        message = request.build_absolute_uri(
            f"{reverse('activate')}?token={token}&uid={uidb64}"
        )
        send_activate_link.delay(user.email, message)


    @staticmethod
    def activate_user(data):
        id = data.get('id')
        user = User.objects.get(id=id)
        user.is_verified = True
        user.save()
        return data
