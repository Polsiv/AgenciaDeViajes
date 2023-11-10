from Colas import *
from Pilas import *

#clase nodo vertice
class nodoArista(object):

#crea un nodo arista con la informacion cargada   
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

#clase nodo vertice
class nodoVertice(object):

#crea un nodo vertice con la informacion cargada
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

#Clase grafo implementacion lista de listas de adyacencia
class Grafo(object):

    #crea un grafo vacio
    def __init__(self, dirigido = True):
        self.inicio = None
        self. dirigido = dirigido
        self.tamanio = 0

#claselista de aristas implementacion sobre lista
class Arista(object):

    #crea una lista de aristas vacia
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
    

#SEGUNDA==============================================

#insertar un vertice al grafo
def insertar_vertice(grafo, dato):
    nodo = nodoVertice(dato)

    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

#inserta una arista desde el vertice origen al destino
def insertar_arista(grafo, dato, origen, destino):
    agregar_arista(origen.adyacentes, dato, destino.info)
    if(not grafo.dirigido):
        agregar_arista(destino.adyacentes, dato, origen.info)

#agregar la arista desde el vertice origen al destino
def agregar_arista(origen, dato, destino):
    nodo = nodoArista(dato, destino)

    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1
    
    
#TERCERAS==============================================


#elimina un vertice del grafo y lo devuelve si lo encuentra
def eliminar_vertice(grafo, clave):    
    x = None

    if (grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        
        if(act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    
    if (x is not None):
        aux = grafo.inicio
        
        while (aux is not None):
            if (aux.adyacentes.inicio is not None):
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
    return x


#Devuelve la direccion del elemento buscado
def buscar_vertice(grafo, buscado):
    aux = grafo.inicio
    while (aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

#Devuelve la direccion del elemento buscado
def buscar_arista(vertice, buscado):
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux

#CUARTA ==========================================================

#Devuelve el numero de vertices en el grafo
def tamanio(grafo):
    return grafo.tamanio

#devuelve true si el grafo esta vacio
def grafo_vacio(grafo):
    return grafo.inicio is None

#elimina una arista del vertice y lo devuelve si lo encuentra
def eliminar_arista(vertice, destino):
    x = None

    if(vertice.inicio.destino == destino):
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig

        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x


#QUINTA ==========================================================

#barrido en la profundidad del grafo
def existe_paso(grafo, origen, destino):
    resultado = False

    if (not origen.vistado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio

        while(vadyacentes is not None and not resultado):
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if (adyacente.info == destino.info):
                return True
            elif (not adyacente.visitado):
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

#muestra los adyacentes del vertice
def adyacentes(vertice):
    aux = vertice.adyacentes.inicio
    
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig
            

#determina si el destino es adyacente directo
def es_adyacente(vertice, destino):
    resultado = False
    aux = vertice.adyacentes.inicio
    
    while (aux is not None and not resultado):
        if (aux.destino == resultado):
            resultado = True
        aux = aux.sig
    
    return resultado



#SEXTA ==========================================================

#Marcar todos los vertices del grafo como no visitados
def marcar_no_visitado(grafo):
    aux = grafo.inicio

    while(aux is not None):
        aux.visitado = False
        aux = aux.sig

#Realiza un barrido del grafo mostrando sus valores
def barrido_vertices(grafo):
    aux = grafo.inicio

    while(aux is not None):
        print(aux.info)
        aux = aux.sig

#Barrido en profundidad del grafo

def barrido_profundidad (grafo, vertice):
    
    while(vertice is not None):
        if (not vertice.visitado):
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio

            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                
                if (not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

#SEPTIMA================================================================

#Barrido en amplitud del grafo 
def barrido_amplitud (grafo, vertice):
    cola = Cola()
    
    while(vertice is not None):
        if (not vertice.visitado):
            vertice.visitado = True
            arribo(cola, vertice)
            
            while(not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if (not adyacente.visitado):
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        
        vertice = vertice.sig


#ALGORITMOS===============================================

#Algoritmo de Dijkstra para hallar el camino mas corto

# def dijkstra(grafo, origen, destino):
#     no_visitados = Heap(tamanio(grafo))