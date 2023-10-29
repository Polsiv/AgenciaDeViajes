class Ciudad(object):
    def __init__(self, nombre, tiempoEstancia):
        self._nombre = nombre
        self._tiempoEstancia = tiempoEstancia
        self._listaActividades = []
    
    def Nombre(self):
        return self._nombre
    
    def TiempoEstancia(self):
        return self._tiempoEstancia
    
    def ListaActividades(self):
        return self._listaActividades
    
    def Nombre(self, nombre):
        self._nombre = nombre
    
    def TiempoEstancia(self, tiempoEstancia):
        self._tiempoEstancia = tiempoEstancia
    
    def ListaActividades(self, listaActividades):
        self._listaActividades = listaActividades
        