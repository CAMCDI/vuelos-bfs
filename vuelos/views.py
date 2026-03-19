from django.shortcuts import render

from .utils import buscar_solucion_BFS, conexiones

def index(request):
    resultado = None
    error = None

    if request.method == "POST":
        origen = request.POST.get('origen','').lower().strip()
        destino = request.POST.get('destino','').lower().strip()

        if origen in conexiones and destino in conexiones:
            nodo_solucion = buscar_solucion_BFS(conexiones,origen,destino)

            if nodo_solucion:
                camino = []
                nodo = nodo_solucion

                while nodo is not None:
                    camino.append(nodo.get_datos())
                    nodo = nodo.get_padre()
                camino.reverse()
                resultado = camino 
            else:
                error="No se encontró camino"
        else:
            error="Ingresa ciudades válidas"
    return render(request, 'vuelos/index.html', {
        'resultado' : resultado,
        'error': error,
        'ciudades': sorted(conexiones.keys())
})
