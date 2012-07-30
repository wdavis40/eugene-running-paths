from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
  return HttpResponse("Hello world")

def home(request):
  return render_to_response('base_home.html', {})

def paths(request):
  return render_to_response('base_paths.html', {})
