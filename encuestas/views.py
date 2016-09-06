from django.shortcuts import get_object_or_404 as findOrFail, render
from django.http import HttpResponse as Respuesta, Http404, HttpResponseRedirect as Redirect
from django.urls import reverse
from .models import Pregunta, Opcion

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
    pregunta = findOrFail(Pregunta, pk=pregunta_id)

    return render(peticion, 'encuestas/resultados.html', {'pregunta': pregunta})

def votar(peticion, pregunta_id):
    pregunta = findOrFail(Pregunta, pk=pregunta_id)

    try:
        opcion = pregunta.opcion_set.get(pk=peticion.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        # Redisplay the question voting form.
        return render(peticion, 'encuestas/detalles.html', {
            'pregunta': pregunta,
            'error_message': "Seleccione una opcion",
        })

    else:
        opcion.votos += 1
        opcion.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return Redirect( reverse('encuestas:resultados', args=(pregunta.id,)) )
