from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Resume
from .serializer import ResumeSerializer

# Create your views here.


class ResumeUploadView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)