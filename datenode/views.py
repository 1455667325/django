from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'datenode/index.html')
def getNode(request):
    request.encoding = 'utf-8'
    name = request.GET.get('name')
    if not name:
        name='小可爱，您还没有写入name；'
    result = {'code': 200, 'data': {'name':name}}
    return HttpResponse(json.dumps(result))
