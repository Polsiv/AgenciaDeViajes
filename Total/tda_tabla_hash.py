from tda_lista import Lista, insertar, tamano, buscar

def crear_tabla(tamano):
    tabla = [None]*tamano
    return tabla


def cantidad_elementos(tabla):
    return len(tabla)-tabla.count(None)


def cantidad_elementos_totales(tabla):
    return sum(tamano(lista) for lista in tabla if lista is not None)


def funcion_hash(dato, tamano_tabla):
    
    return len(str(dato).strip()) % tamano_tabla


def agregar(tabla, dato):
    posicion = funcion_hash(dato.usuario, len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)


def buscar_tabla(tabla, buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if(tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos
