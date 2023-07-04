from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.utils.http import urlsafe_base64_decode

from apps.users.serializers import LoginSerializer, UserAcivationSerializer, UserRegistrationSerializer
from apps.users.services import ActivationService, LoginService


class LoginView(APIView):
    permission_classes = (AllowAny,)


    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = LoginService.login_user(data=serializer.data)
            if data:
                return Response(data=data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(APIView):
    permission_classes = (AllowAny,)


    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



class ActivationView(APIView):
    permission_classes = (AllowAny,)


    def get(self, request, *args, **kwargs):
        uid = request.query_params.get("uid")
        id = urlsafe_base64_decode(uid).decode()
        token = request.query_params.get("token")
        data = {
            "id": id,
            "token": token
        }
        serializer = UserAcivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            data = ActivationService.activate_user(serializer.data)
            return Response(data=data, status=200)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




       
        
