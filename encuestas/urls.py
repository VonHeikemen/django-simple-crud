from django.conf.urls import url
from . import views

#Namespace para los nombres de las rutas
app_name = 'encuestas'
urlpatterns = [
	# ej: /encuestas/
	url(r'^$', views.index, name='index'),

	# ej: /encuestas/5/
	url(r'^(?P<pregunta_id>[0-9]+)/$', views.detalles, name='detalles'),
	
	# ej: /encuestas/5/resultados/
	url(r'^(?P<pregunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
	
	# ej: /encuestas/5/votar/
	url(r'^(?P<pregunta_id>[0-9]+)/votar/$', views.votar, name='votar'),
]