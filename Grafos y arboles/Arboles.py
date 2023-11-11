from Colas import *

class nodoArbol(object):
    #Crea un nodo con la informacion cargada
    def __init__(self, info) :
        self.izq = None
        self.der = None
        self.info = info
    
#elimina un elemento del arbol y lo devuelve si lo encuentra
def eliminar_nodo(raiz, clave):
    x = None
    
    if (raiz is not None):
        if (clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            
            if(raiz.izq is None):
                raiz = raiz.der
            elif (raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info

    return raiz, x

#Inserta un dato al arbol
def insertar_nodo(raiz, dato):
    if (raiz is None):
        raiz = nodoArbol(dato)
    elif (dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

#Devuelve true si el arbol esta vacio

def arbolvacio(raiz):
    return raiz is None


#SEGUNDA===========================================================


#determina el nodo que reemplazara al que se elimina
def reemplazar(raiz):
    aux = None
    
    if (raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    
    return raiz, aux

#realiza el barrido postorden del arbol
def por_nivel(raiz):
    pendientes = Cola()
    arribo(pendientes, raiz)

    while (not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)

        if(nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)

#devuelve la direccion del elemento buscado
def buscar(raiz, clave):
    pos = None

    if (raiz is not None):
        if (raiz.info == clave):
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos

#TERCERA===========================================================

#Realiza el barrido inorden del arbol
def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

#realiza el barrido preorden del arbol
def preorden(raiz):
    if (raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

#realiza el barrido postorden del arbol
def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)
    



