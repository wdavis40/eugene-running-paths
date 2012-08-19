from django.http import HttpResponse
from django.shortcuts import render_to_response
from paths.models import Path

def index(request):
  paths = Path.objects.all()
  return render_to_response('paths/base_paths.html', {'paths': paths})

