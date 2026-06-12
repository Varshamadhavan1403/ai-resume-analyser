from django.db import models
from django.conf import settings
# Create your models here.


class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resumes')
    file = models.FileField(upload_to='resumes/')
    parsed_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_skills = models.JSONField(default=list, blank=True)
    score = models.IntegerField(default=0)
    experience_years = models.IntegerField(default=0)
    companies = models.JSONField(default=list, blank=True)
    education = models.JSONField(default=list, blank=True)
    def __str__(self):
        return self.file.name
