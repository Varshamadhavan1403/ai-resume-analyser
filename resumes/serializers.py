from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"
        read_only_fields = ['user']


class ResumeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'extracted_skills', 
                  'score', 'experience_years', 'companies', 'education',]