from django.db import models

class Pregunta(models.Model):
	pregunta_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('fecha de publicacion')

class Opcion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	opcion_text = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)
