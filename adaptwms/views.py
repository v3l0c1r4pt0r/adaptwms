import logging
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from adaptwms.translator import Translator

translator = Translator()

def interface_view(request):
  return HttpResponse("Hello, Django!", content_type="text/plain")

def test_handler(url):
  return HttpResponse(url, content_type="text/plain")

def redirect_handler(url):
  logging.info(f'Redirecting to {url}')
  return redirect(url)

def fetch_handler(url):
  r = requests.get(url)
  logging.info(f'Fetched {url} for you (got type: {r.headers["content-type"]})')
  response = HttpResponse(r.content, content_type=r.headers['content-type'])
  return response

handlers = {
  'test': test_handler,
  'redirect': redirect_handler,
  'fetch': fetch_handler,
}

def adapter_view(request):
  params = request.GET

  try:
    x = int(params['x'])
    y = int(params['y'])
    z = int(params['z'])

    template = params['template']
  except MultiValueDictKeyError as e:
    return HttpResponse(f"Missing required parameter: {e.args[0]}", content_type="text/plain")
  if 'mode' in params:
    mode = params['mode']
  else:
    mode = 'redirect'

  url = translator.translate(x, y, z, template)

  response = handlers[mode](url)

  return response
