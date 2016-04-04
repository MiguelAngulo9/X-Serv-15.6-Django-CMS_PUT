from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request, peticion_id):

    try:
        solicitud = Pages.objects.get(id=int(peticion_id))
        #en vez del id lo podemos hacer tambien con el nombre pero esta mejor asi
    except Pages.DoesNotExist:
        return HttpResponse('Page Not Found')
    respuesta = 'Hola, soy ' + solicitud.name + ": " + str(solicitud.page)
    return HttpResponse(respuesta)

@csrf_exempt
def paginanueva(request, nombre, pagina):
    if request.method == "GET":
        p = Pages(name=nombre, page=pagina)
        p.save()
    elif request.method == "PUT":
        info = request.body
        p = Pages(name=nombre, page=info)
        p.save()
    return HttpResponse('Todo ha ido bien')

def dame_paginas(request):
    lista_paginas = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista_paginas:
        respuesta += '<li><a href="/cmsput/' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
