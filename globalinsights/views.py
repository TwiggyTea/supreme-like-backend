from globalinsights.models import Global
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GlobalSerializer

from .models import Global
# Create your views here.

@api_view(['GET'])
def globalDetail(request):
    globals = Global.objects.all()
    serializers = GlobalSerializer(globals, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def globalCreate(request):
    serializers = GlobalSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def globalUpdate(request, pk):
    globals = Global.objects.get(id=pk)
    serializers = GlobalSerializer(instance=globals, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)