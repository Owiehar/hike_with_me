from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'Hike, Run, Cycle, Camp!'}
    return render(request, 'hike/index.html', context=context_dict)
