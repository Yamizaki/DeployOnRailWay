from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import redirect
from .forms import ContactForm

def solicitud(request):
    asunto =request.GET['asunto']
    if request.method == "GET":

        asunto =request.GET['asunto']
        ref=request.GET['ref']
        solicitado=request.GET['solicitado']
        cargo_solicitado=request.GET['cargo_solicitado']
        atencion=request.GET['atencion']
        solicitante=request.GET['solicitante']
        dni=request.GET['dni']
        direccion=request.GET['direccion']
        distrito=request.GET['distrito']
        provincia=request.GET['provincia']
        departamento=request.GET['departamento']  
        cargo_solicitante=request.GET['cargo_solicitante'] 
        cabeza_solicitud=request.GET['cabeza_solicitud']
        cuerpo_solicitud=request.GET['cuerpo_solicitud']
        celular=request.GET['celular']
        fecha=request.GET['fecha']

    
        

        return render (request, "plantilla.html",{
            "ASUNTO":   asunto,
            "REFERENCIA": ref,
            "SOLICITADO": solicitado,
            "CARGOSOLICITADO": cargo_solicitado,
            "ATENCION": atencion,
            "SOLICITANTE": solicitante, 
            "DOCUMENTOSOLICITANTE": dni,
            "DIRECCIONSOLICITANTE": direccion,
            "DISTRITO":distrito,
            "PROVINCIA": provincia,
            "DEPARTAMENTO": departamento,
            "CARGOSOLICITANTE": cargo_solicitante,
            "CELULAR": celular,
            "FECHA": fecha,
            "SOLICITUD_CABEZA":cabeza_solicitud,
            "SOLICITUD_CUERPO":cuerpo_solicitud
        }) 
    else:
        return HttpResponse("Algo salio mal")




def contact_view(request):
    formulario= ContactForm()
    return render (request,'contact.html',{"formulario":formulario})