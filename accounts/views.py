from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email,
        })
# Create your views here.
