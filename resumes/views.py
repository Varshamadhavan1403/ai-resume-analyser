from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeSerializer
from . services import ResumeParser
from .skill_extractor import SkillExtractor
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .analyzer import ResumeAnalyzer

# Create your views here.


class ResumeUploadView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = serializer.save(user=self.request.user)
        # extracted_text = ResumeParser.parse(resume.file.path)
        # resume.parsed_text = extracted_text
        # resume.save()
        parsed_text = ResumeParser.parse(resume.file.path)
        skills = SkillExtractor.extract(parsed_text)
        resume.parsed_text = parsed_text
        resume.extracted_skills = skills
        analysis = ResumeAnalyzer.analyze(skills)
        resume.score = analysis['score']
        # resume.missing_skills = analysis['missing_skills']
        resume.save()


class ResumeDetailView(generics.RetrieveAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)
    

class ResumeListView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)
    

class ResumeSkillsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        resume = get_object_or_404(Resume, user=request.user, pk=pk)
        return Response ({ "skills": resume.extracted_skills , "resume_id": resume.id})
        

class ResumeAnalysisView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        resume = get_object_or_404(Resume, user=request.user, pk=pk)
        analysis = ResumeAnalyzer.analyze(resume.extracted_skills)
        return Response({
            "score": resume.score,
            "missing_skills": analysis['missing_skills'],
            "resume_id": resume.id,
            "skills": resume.extracted_skills
        })