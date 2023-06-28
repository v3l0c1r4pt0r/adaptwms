from django.shortcuts import render
from django.http import HttpResponse

def interface_view(request):
  return HttpResponse("Hello, Django!", content_type="text/plain")
