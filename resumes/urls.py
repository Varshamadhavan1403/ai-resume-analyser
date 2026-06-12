from .views import (
    ResumeUploadView, ResumeDetailView, ResumeListView, ResumeSkillsView, 
    ResumeAnalysisView, ResumeProfileView
)
from django.urls import path

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('', ResumeListView.as_view(), name='resume-list'),
    path('<int:pk>/skills/', ResumeSkillsView.as_view(), name='resume-skills'),
    path('<int:pk>/analysis/', ResumeAnalysisView.as_view(), name='resume-analysis'),
    path('<int:pk>/profile/', ResumeProfileView.as_view(), name='resume-profile'),
]
