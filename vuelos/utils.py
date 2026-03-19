class Nodo:
    def  __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.costo = None
    
    def set_hijos (self, hijos):
        self.hijos = hijos 
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self
    def get_hijos (self):
        return self.hijos

    def get_padre(self):
        return self.padre
    
    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self,datos):
        self.datos = datos

    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo
    
    def igual (self, nodo):
        if self.get_datos () == nodo.get_datos():
            return True
        else:
            return False
        
    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
               en_la_lista = True
        return en_la_lista
    
    def _str_ (self):
        return str(self.get_datos())

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera[0]
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) \
                    and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)

conexiones = {
    'jiloyork': {'celaya', 'cdmx', 'queretaro'},
    'sonora': {'zacatecas', 'sinaloa'},
    'guanajuato': {'aguascalientes'},
    'oaxaca': {'queretaro'},
    'sinaloa': {'celaya', 'sonora', 'jiloyork'},
    'queretaro': {'tamaulipas', 'zacatecas', 'sinaloa', 'jiloyork', 'oaxaca'},
    'celaya': {'jiloyork', 'sinaloa'},
    'zacatecas': {'sonora', 'monterrey', 'queretaro'},
    'monterrey': {'zacatecas', 'sinaloa'},
    'tamaulipas': {'queretaro'},
    'cdmx': {'jiloyork', 'guanajuato', 'aguascalientes'},
    'aguascalientes': {'cdmx', 'guanajuato', 'jiloyork'}
}
