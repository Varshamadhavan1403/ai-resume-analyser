from .views import ResumeUploadView
from django.urls import path

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),]
