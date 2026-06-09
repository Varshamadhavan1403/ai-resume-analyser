from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeSerializer
from . services import ResumeParser

# Create your views here.


class ResumeUploadView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = serializer.save(user=self.request.user)
        extracted_text = ResumeParser.parse(resume.file.path)
        resume.parsed_text = extracted_text
        resume.save()