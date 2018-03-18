from rest_framework import serializers
from .models import RiskType, RiskField

class RiskFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskField
        fields = '__all__'
       
class RiskTypeSerializer(serializers.ModelSerializer):
    fields = RiskFieldSerializer(many=True, read_only=True)

    class Meta:
        model = RiskType
        fields = '__all__'
       
