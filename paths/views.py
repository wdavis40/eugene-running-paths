from django.http import HttpResponse
from django.shortcuts import render_to_response
from paths.models import Path

def index(request):
  paths = Path.objects.all()
  return render_to_response('paths/base_paths.html', {'paths': paths})

def path(request, path_id):
  try:
    path_id = int(path_id)
  except ValueError:
    raise Http404()
  path = Path.objects.get(pk=path_id)
  return render_to_response('paths/path.html', {'path': path})
