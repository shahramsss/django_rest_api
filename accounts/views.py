from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle 


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


class UserViewset(viewsets.ViewSet):
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # throttle_scope = "questions"
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    queryset = User.objects.all()

    def list(self, request):
        ser_data = UserSerializer(instance=self.queryset, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerializer(instance=user)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({"messages": "Permission denied: you are not owner!"})
        ser_data = UserSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        if user != request.user:
            return Response({"messages": "Permission denied: you are not owner!"})
        user.is_active = False
        user.save()
        return Response({"message": "user deactivated"})
