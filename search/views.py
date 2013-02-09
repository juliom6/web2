from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from search.models import Publicacion

def buscador(request):
    return render_to_response('search_engine.html', {}, context_instance = RequestContext(request))
def resultados(request):
    if 'q' in request.GET:
		q = request.GET['q']
		publicaciones = Publicacion.objects.filter(titulo__icontains = q)
		lista = ({'nombre': 'computacion', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'computacion').count()},
			{'nombre': 'celulares', 'cantidad':Publicacion.objects.filter(descripcion__icontains = 'celular').count()},
			{'nombre': 'audio', 'cantidad':Publicacion.objects.filter(descripcion__icontains = 'audio').count()},
			{'nombre': 'video', 'cantidad':Publicacion.objects.filter(descripcion__icontains = 'video').count()},
			{'nombre': 'libros', 'cantidad':Publicacion.objects.filter(descripcion__icontains = 'libro').count()},
		)
		#lista = ('computacion','celulares','audio','video','libros')
		#lista = {	('computacion', Publicacion.objects.filter(descripcion__icontains = 'computacion').count()), 
		#		('celulares', Publicacion.objects.filter(descripcion__icontains = 'celulares').count()), 
		#		('usb', Publicacion.objects.filter(descripcion__icontains = 'usb').count()), 
		#		'audio': Publicacion.objects.filter(descripcion__icontains = 'audio').count(), 
		#		'video': Publicacion.objects.filter(descripcion__icontains = 'video').count(), 
		#		'libros': Publicacion.objects.filter(descripcion__icontains = 'libros').count(), 
		#	}
		#c1 = Publicacion.objects.filter(descripcion__icontains = 'audio').count()
		#c2 = Publicacion.objects.filter(descripcion__icontains = 'video').count()
		i = Publicacion.objects.filter(descripcion__icontains = 'computacion').count()
		return render_to_response('resultados_busqueda2.html', {'lista': lista, 'total_computacion': i, 'publicaciones': publicaciones, 'consulta': q})
        #mensaje = 'Acabas de buscar el termino: %r' % request.GET['q']
    else:
        #mensaje = 'Enviaste una busqueda vacia'
    	return HttpResponse('Por favor envia un termino de busqueda.')
def audioyvideo(request):
	lista = ({'nombre': 'audio', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'audio').count()},
		{'nombre': 'video', 'cantidad':Publicacion.objects.filter(descripcion__icontains = 'video').count()},
	)
	#return render_to_response('audioyvideo.html', {'audiocantidad': c1, 'videocantidad': c2})
	return render_to_response('resultados_busqueda2.html', {'lista': lista, 'consulta': 'audio y video'})
def audio(request):
	lista = ({'nombre': 'audio', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'audio').count()})
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'audio')
	return render_to_response('resultados_busqueda2.html', { 'publicaciones': publicaciones, 'consulta': 'audio'})
def video(request):
	lista = ({'nombre': 'video', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'video').count()})
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'video')
	return render_to_response('resultados_busqueda2.html', {'publicaciones': publicaciones,})
def celulares(request):
	lista = ({'nombre': 'celulares', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'celular').count()})
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'celular')
	return render_to_response('resultados_busqueda2.html', {'publicaciones': publicaciones, 'consulta': 'celulares'})
def computacion(request):
	lista = ({'nombre': 'computacion', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'usb').count()})
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'usb') #solo para pruebas, hay que cambiar este tag
	return render_to_response('resultados_busqueda2.html', {'publicaciones': publicaciones, 'consulta': 'usb'})
def libros(request):
	lista = ({'nombre': 'libros', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'libro').count()})
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'libro')
	return render_to_response('resultados_busqueda2.html', {'publicaciones': publicaciones, 'consulta': 'libro'})
def instrumentosmusicales(request):
	lista = ({'nombre': 'instrumentosmusicales', 'cantidad': Publicacion.objects.filter(descripcion__icontains = 'musica').count()})
	publicaciones = Publicacion.objects.filter(descripcion__icontains = 'musica')
	return render_to_response('resultados_busqueda2.html', {'publicaciones': publicaciones, 'consulta': 'celulares'})
def producto(request, id_producto):
	id_producto = int(id_producto)
	publicacion = Publicacion.objects.get(id = id_producto)
	return render_to_response('mostrar_producto.html', {'publicacion': publicacion})
