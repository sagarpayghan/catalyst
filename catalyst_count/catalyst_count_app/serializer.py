from rest_framework import serializers
from .models import CompanyModel

class CompanySerializer(serializers.Serializer):
    class Meta:
        model=CompanyModel
        fields='__all__'
