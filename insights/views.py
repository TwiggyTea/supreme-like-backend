from insights.models import Insight
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InsightSerializer

from .models import Insight
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/insight-list/',
        'Detail View': '/insight-detail/<str:pk>/',
        'Create': '/insight-create/',
        'Update': '/insight-update/<str:pk>/',
        'Delete': '/insight-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def insightList(request):
    insights = Insight.objects.all()
    serializers = InsightSerializer(insights, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def insightDetail(request, pk):
    insights = Insight.objects.get(id=pk)
    serializers = InsightSerializer(insights, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def insightCreate(request):
    serializers = InsightSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def insightUpdate(request, pk):
    insights = Insight.objects.get(id=pk)
    serializers = InsightSerializer(instance=insights, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def insightDelete(request, pk):
    insights = Insight.objects.get(id=pk)
    insights.delete()
    return Response("item deleted")