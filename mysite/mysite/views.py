from django.http import HttpResponse
from django.template import Template,Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render
class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellidos=apellido
def saludo(request):
    p1=Persona("Hadad","Bautista García")
    #doc_externo=open("./mysite/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=get_template("miplantilla.html")
    ahora=datetime.datetime.now()
    temas=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    ctx={"persona":p1,"apellido":p1.apellidos,"momento_actual":ahora,"temas":temas}
    #documento=doc_externo.render(ctx)
    return render(request, "miplantilla.html",ctx)
def despedida(request):
    return HttpResponse("Adios")
def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>
    """ %fecha_actual
    return HttpResponse(documento)
def calculaEdad(request,edad,agno):
    edadActual=edad
    periodo=agno-2020
    edadFutura=edadActual+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendras %s años
    </h1>
    </body>
    </html>
    """ %(agno,edadFutura)
    return HttpResponse(documento)
def cursoCss(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"CursoCss.html",{"dameFecha":fecha_actual})

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"CursoC.html",{"dameFecha":fecha_actual})


