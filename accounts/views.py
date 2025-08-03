from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from rest_framework import status


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
        if ser_data.is_valid():
            # User.objects.create_user(
            #     username=ser_data.validated_data["username"],
            #     email=ser_data.validated_data["email"],
            #     password=ser_data.validated_data["password"],
            # )
            ser_data.create(ser_data.validated_data)
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
