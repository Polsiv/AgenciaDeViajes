class Pais(object):
    def __init__(self, nombre, ciudad):
        self._nombre = nombre
        self._ciudad = ciudad
    
    def Nombre(self):
        return self._nombre
    
    def Ciudad(self):
        return self._ciudad
    
    def Nombre(self, nombre):
        self._nombre = nombre
        
    def Ciudad(self, ciudad):
        self._ciudad = ciudad
        
class Destino(Pais):
    def __init__(self, nombre, ciudad, hospedaje, tiempoEstancia, costo, listaActividades):
        super().__init__(nombre, ciudad)
        self._hospedaje = hospedaje
        self._tiempoEstancia = tiempoEstancia
        self._costo = costo
        self._listaActividades = listaActividades
        