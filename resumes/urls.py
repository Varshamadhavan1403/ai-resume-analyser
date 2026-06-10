from .views import ResumeUploadView, ResumeDetailView, ResumeListView, ResumeSkillsView
from django.urls import path

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path('<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('', ResumeListView.as_view(), name='resume-list'),
    path('<int:pk>/skills/', ResumeSkillsView.as_view(), name='resume-skills'),
]
