from insurers.models import RiskType, RiskField
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from insurers.serializers import RiskTypeSerializer, RiskFieldSerializer
from rest_framework.response import Response

class RiskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Risks.
    """
    queryset=""
    def list(self, request):
        queryset = RiskType.objects.all()
        serializer = RiskTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=id):
        queryset = RiskType.objects.all()
        user = get_object_or_404(queryset, id=id)
        serializer = RiskTypeSerializer(user)
        return Response(serializer.data)

risk_list = RiskViewSet.as_view({'get': 'list'})
risk_detail = RiskViewSet.as_view({'get': 'retrieve'})    
