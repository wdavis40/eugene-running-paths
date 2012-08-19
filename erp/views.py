from django.http import HttpResponse
from django.shortcuts import render_to_response
from paths.models import Path

def home(request):
  return render_to_response('base_home.html', {})

def paths(request):
  paths = Path.objects.all()
  return render_to_response('base_paths.html', {'paths': paths})

def about(request):
  return render_to_response('base_about.html', {})
