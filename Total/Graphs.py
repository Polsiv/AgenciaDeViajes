from Colas import *
from Pilas import *
import streamlit as st
import math
from heapq import heappush, heappop
from login import mostrar_info
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
        self.distancia = float('inf')
        self.anterior = None

#Clase grafo implementacion lista de listas de adyacencia
class Grafo(object):

    #crea un grafo vacio
    def __init__(self, dirigido = False):
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
    origenAux= buscar_vertice(grafo, origen)
    destinoAux= buscar_vertice(grafo,destino)
    agregar_arista(origenAux.adyacentes, dato, destinoAux.info)
    if(not grafo.dirigido):
        agregar_arista(destinoAux.adyacentes, dato, origenAux.info)

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

    if (not origen.visitado):
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
        peso=aux.info.split("/")
        costo=int(peso[0])
        tiempo=int(peso[1])
        #print(f"Arista a {aux.destino}: Costo ${costo} - Horas: {tiempo}h")
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
        #print(aux.info)
        adyacentes(aux)
        #print("----------")
        aux = aux.sig

#Barrido en profundidad del grafo

def barrido_profundidad (grafo, vertice):
    auxVertice = buscar_vertice(grafo, vertice)

    while(auxVertice is not None):
        if (not auxVertice.visitado):
            auxVertice.visitado = True
            print(auxVertice.info)
            adyacentes = auxVertice.adyacentes.inicio

            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)

                if (not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        auxVertice = auxVertice.sig

#SEPTIMA================================================================

#Barrido en amplitud del grafo 
def barrido_amplitud (grafo, vertice):
    cola = Cola()
    auxVertice = buscar_vertice(grafo, vertice)

    while(auxVertice is not None):
        if (not auxVertice.visitado):
            auxVertice.visitado = True
            arribo(cola, auxVertice)

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

        auxVertice = auxVertice.sig
#ALGORITMOS===============================================

#Algoritmo de Dijkstra para hallar el camino mas corto
#----------------------------------------------------------------------------------------

def dijkstraCosto(grafo, origen, destino):
    no_visitado = []
    actual = None
    aux = grafo.inicio

    marcar_no_visitado(grafo)

    while aux is not None:
        if aux.info != origen:
            no_visitado.append(aux)
        else:
            aux.distancia = 0
            actual = aux
            no_visitado.append(aux)

        aux = aux.sig

    const = 0
    while const < 5:
        #print("Actualmente estoy en: " + actual.info)
        #print("--------------------------------------------")
        adyacentes = actual.adyacentes.inicio
        

        while adyacentes is not None:
            verticeAdyacente = buscar_vertice(grafo, adyacentes.destino)

            if not verticeAdyacente.visitado:
                #print("Soy un vertice: " + verticeAdyacente.info)
                #print("----------------------------")
                #print("Soy el vertice: " + verticeAdyacente.info + " con distancia: " + str(verticeAdyacente.distancia))
                #print("La distancia hacia el vertice: " + verticeAdyacente.info + " es: " + str(actual.distancia + int(adyacentes.info.split("/")[0])))
                #print("----------------------------")

                if actual.distancia + int(adyacentes.info.split("/")[0]) < verticeAdyacente.distancia:
                    verticeAdyacente.distancia = actual.distancia + int(adyacentes.info.split("/")[0])
                    verticeAdyacente.anterior = actual

            adyacentes = adyacentes.sig

        actual.visitado = True
        no_visitado.remove(actual)

        menor = float('inf')
        aristaMenor = None
        adyacentes = actual.adyacentes.inicio

        while adyacentes is not None:
            verticeAdyacente = buscar_vertice(grafo, adyacentes.destino)

            if not verticeAdyacente.visitado:
                if int(adyacentes.info.split("/")[0]) < menor:
                    menor = int(adyacentes.info.split("/")[0])
                    aristaMenor = adyacentes

            adyacentes = adyacentes.sig

        if aristaMenor is not None:
            nuevoActual = buscar_vertice(grafo, aristaMenor.destino)
            actual = nuevoActual
            #print("Nuevo actual: " + actual.info)

        barrido_vertices(grafo)
        const += 1

    destino = buscar_vertice(grafo, destino)
    print("-"*45)
    if destino is not None:
        print("Costo total del recorrido hasta el destino: ", destino.distancia)
        print("-"*45)
        print("El camino mas barato para llegar de ", origen, " a ", destino.info, "Es") 
        while destino is not None:
            print("-",destino.info)
            destino = destino.anterior\
        
    else:
        print("No se encontró un camino hasta el destino.")


def dijkstraDistancia(grafo, origen, destino):
    no_visitado = []
    actual = None
    aux = grafo.inicio

    marcar_no_visitado(grafo)

    while aux is not None:
        if aux.info != origen:
            no_visitado.append(aux)
        else:
            aux.distancia = 0
            actual = aux
            no_visitado.append(aux)

        aux = aux.sig

    const = 0
    while const < 5:
        #print("Actualmente estoy en: " + actual.info)
        #print("--------------------------------------------")
        adyacentes = actual.adyacentes.inicio
        

        while adyacentes is not None:
            verticeAdyacente = buscar_vertice(grafo, adyacentes.destino)

            if not verticeAdyacente.visitado:
                #print("Soy un vertice: " + verticeAdyacente.info)
                #print("----------------------------")
                #print("Soy el vertice: " + verticeAdyacente.info + " con distancia: " + str(verticeAdyacente.distancia))
                #print("La distancia hacia el vertice: " + verticeAdyacente.info + " es: " + str(actual.distancia + int(adyacentes.info.split("/")[1])))
                #print("----------------------------")

                if actual.distancia + int(adyacentes.info.split("/")[1]) < verticeAdyacente.distancia:
                    verticeAdyacente.distancia = actual.distancia + int(adyacentes.info.split("/")[1])
                    verticeAdyacente.anterior = actual

            adyacentes = adyacentes.sig

        actual.visitado = True
        no_visitado.remove(actual)

        menor = float('inf')
        aristaMenor = None
        adyacentes = actual.adyacentes.inicio

        while adyacentes is not None:
            verticeAdyacente = buscar_vertice(grafo, adyacentes.destino)

            if not verticeAdyacente.visitado:
                if int(adyacentes.info.split("/")[1]) < menor:
                    menor = int(adyacentes.info.split("/")[1])
                    aristaMenor = adyacentes

            adyacentes = adyacentes.sig

        if aristaMenor is not None:
            nuevoActual = buscar_vertice(grafo, aristaMenor.destino)
            actual = nuevoActual
            #print("Nuevo actual: " + actual.info)

        barrido_vertices(grafo)
        const += 1

    destino = buscar_vertice(grafo, destino)
    lista_destinos = []
    print("-"*45)
    if destino is not None:
        print("Distancia (en horas) total del recorrido hasta el destino: ", destino.distancia)
        print("-"*45)
        print("El camino mas corto en horas para llegar de ", origen, " a ", destino.info, "Es")  
        while destino is not None:
            
            print("-",destino.info)
            lista_destinos.append(destino.info)
            destino = destino.anterior
    else:
        print("No se encontró un camino hasta el destino.")
    
    def mostrar_info():
        st.write("Distancia (en horas) total del recorrido hasta el destino: ", destino.distancia)
        st.write("El camino mas corto en horas para llegar de ", origen, " a ", destino.info, "Es")  
        for i in lista_destinos:
            st.write(i)

    
        
def dijkstraDistanciaMasLarga(grafo, origen, destino):
    no_visitado = []
    actual = None
    aux = grafo.inicio

    marcar_no_visitado(grafo)

    while aux is not None:
        if aux.info != origen:
            no_visitado.append(aux)
        else:
            aux.distancia = 0
            actual = aux
            no_visitado.append(aux)

        aux = aux.sig

    const = 0
    while const < 5 and no_visitado:  
        adyacentes = actual.adyacentes.inicio

        while adyacentes is not None:
            verticeAdyacente = buscar_vertice(grafo, adyacentes.destino)

            if not verticeAdyacente.visitado:
                if actual.distancia + int(adyacentes.info.split("/")[1]) > verticeAdyacente.distancia:
                    verticeAdyacente.distancia = actual.distancia + int(adyacentes.info.split("/")[1])
                    verticeAdyacente.anterior = actual

            adyacentes = adyacentes.sig

        actual.visitado = True
        if actual in no_visitado:  # Agrega un chequeo para evitar error de lista.remove
            no_visitado.remove(actual)

        mayor = -1  # Valor inicial para la distancia más larga
        aristaMayor = None
        adyacentes = actual.adyacentes.inicio

        while adyacentes is not None:
            verticeAdyacente = buscar_vertice(grafo, adyacentes.destino)

            if not verticeAdyacente.visitado:
                if int(adyacentes.info.split("/")[1]) > mayor:
                    mayor = int(adyacentes.info.split("/")[1])
                    aristaMayor = adyacentes

            adyacentes = adyacentes.sig

        if aristaMayor is not None:
            nuevoActual = buscar_vertice(grafo, aristaMayor.destino)
            actual = nuevoActual

        barrido_vertices(grafo)
        const += 1

    destino = buscar_vertice(grafo, destino)
    print("-"*45)
    if destino is not None:
        print("Distancia (en horas) total de la ruta más larga hasta el destino: ", destino.distancia)
        print("-"*45)
        print("La ruta más larga en horas para llegar de ", origen, " a ", destino.info, "es")  
        while destino is not None:
            print("-", destino.info)
            destino = destino.anterior
    else:
        print("No se encontró una ruta hasta el destino.")




