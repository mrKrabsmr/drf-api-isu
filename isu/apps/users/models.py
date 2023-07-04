from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from apps.category.models import Category


class CustomUserManager(BaseUserManager):

    def create_superuser(self, first_name, last_name, email, password):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=220, null=True, blank=True)
    last_name = models.CharField(max_length=220, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_company = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="media/user_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ("first_name", "last_name", "password")

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("last_name", "first_name")

    def save(self, *args, **kwargs) -> None:
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        if self.company:
            return self.company_info.name
        else:
            return f"{self.first_name} {self.last_name}"
    

class CompanyInfo(models.Model): 
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='company_info')
    name = models.CharField(max_length=220)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="companies")

    class Meta:
        db_table = "companies_info"
        verbose_name = "company_info"
        verbose_name_plural = "companies_info"


    def __str__(self) -> str:
        return self.name





