import datetime
from django.db import models
from django.utils import timezone

class Pregunta(models.Model):
	pregunta_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('fecha de publicacion')

	def __str__(self):
		return self.pregunta_text

	def es_reciente(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Opcion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	opcion_text = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.opcion_text
