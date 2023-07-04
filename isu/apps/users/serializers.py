from rest_framework import serializers
from django.db.transaction import atomic

from apps.users.models import CompanyInfo, User
from apps.users.services import ActivationService, RegistrationService
from apps.users.utils import get_token_func


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)

    
    
class CompanyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyInfo
        fields = '__all__'
    
    @atomic
    def create(self, validated_data):
        return super().create(validated_data)


class UserRegistrationSerializer(serializers.ModelSerializer):
    company_info = CompanyInfoSerializer(read_only=True, required=False)
    token = serializers.SerializerMethodField(read_only=True)
    company_name = serializers.CharField(write_only=True, required=False)
    description = serializers.CharField(write_only=True, required=False)
    category = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'
    
    @atomic
    def create(self, validated_data):
        user = RegistrationService.user_registration(validated_data)
        if user:
            ActivationService.send_activation_mail(
                request=self.context.get("request"), 
                user=user
            )
        return user


    def get_token(self, user):
        return get_token_func(user)
    


class UserAcivationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    token = serializers.CharField()

    



    