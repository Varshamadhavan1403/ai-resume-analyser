from .views import (
    ResumeUploadView, ResumeDetailView, ResumeListView, ResumeSkillsView, 
    ResumeAnalysisView, ResumeProfileView, ResumeSummaryView, JobMatchView,
    DashboardView
)
from django.urls import path

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('', ResumeListView.as_view(), name='resume-list'),
    path('<int:pk>/skills/', ResumeSkillsView.as_view(), name='resume-skills'),
    path('<int:pk>/analysis/', ResumeAnalysisView.as_view(), name='resume-analysis'),
    path('<int:pk>/profile/', ResumeProfileView.as_view(), name='resume-profile'),
    path('<int:pk>/summary/', ResumeSummaryView.as_view(), name='resume-summary'),
    path('jobs/match/', JobMatchView.as_view(), name='job-match'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
