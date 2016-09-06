from django.shortcuts import get_object_or_404 as findOrFail, render
from django.http import HttpResponse as Respuesta, Http404
from .models import Pregunta

def index(peticion):
	lista = Pregunta.objects.order_by('-pub_date')[:5]
	context = {
		'lista': lista
	}
	
	return render(peticion, 'encuestas/index.html', context)

def detalles(peticion, pregunta_id):
	pregunta = findOrFail(Pregunta, pk=pregunta_id)
	context = {
		'pregunta': pregunta
	}

	return render(peticion, 'encuestas/detalles.html', context)

def resultados(peticion, pregunta_id):
	mensaje = "Resultado de la pregunta %s."
	
	return Respuesta(mensaje % pregunta_id)

def votar(peticion, pregunta_id):
	return Respuesta("Estas votando en la pregunta %s." % pregunta_id)
