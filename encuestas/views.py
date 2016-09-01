from django.shortcuts import render
from django.http import HttpResponse as respuesta

def index(peticion):
	return respuesta("Hola, mundo. Estas en el index de las Encuestas.")
