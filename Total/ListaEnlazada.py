class nodoLista(object):
    info, sig = None, None

class Lista(object):
    def __init__ (self):
        self.inicio = None
        self.tamano = 0

def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato
    
    if(lista.inicio is None) or (lista.inicio.info > dato):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig

        while(act is not None and act.info < dato):
            ant = ant.sig
            act = act.sig

        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1

    if (lista.inicio is None) or (lista.inicio.info > dato):
        nodo.sig = lista.inicio
        lista.inicio = nodo

    else:
        ant = lista.inicio
        act = lista.inicio.sig

        while(act is not None and act.info < dato):
            ant = ant.sig
            act = act.sig

        nodo.sig = act
        act.sig = nodo

def lista_vacia(lista):
    return lista.inicio is None

def tamano(lista):
    return lista.tamano


def eliminar(lista, clave):
    dato = None
    
    if(lista.inicio.info == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamano -= 1

    else:
        anterior = lista.inicio
        actual = lista.inicio.sig

        while(actual is not None and actual.info != clave):
            anterior = anterior.sig
            actual = actual.sig

        if(actual is not None):
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamno -= 1

    return dato


def buscar(lista, buscado):
    aux = lista.inicio

    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def barrido(lista):
    aux = lista.inicio
    while (aux is not None):
        print(aux.info)
        aux = aux.sig