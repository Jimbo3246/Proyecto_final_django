from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def inicio(request):
   contexto= {}
   http_responde = render(
      request=request,
      template_name='control_productos/index.html',
      context=contexto,
   )
   return http_responde