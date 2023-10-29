"""
clase
    PlanViaje

atributos
    fechaInicio
    fechaFin
    origen
    paradas
    destino
    costo
"""

class PlanViaje(object):
    def __init__(self, fechaInicio, fechaFin, origen, paradas, destino, costo):
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin
        self._origen = origen
        self._paradas = paradas
        self._destino = destino
        self._costo = costo
        
    def FechaInicio(self):
        return self._fechaInicio
    
    def FechaFin(self):
        return self._fechaFin
    
    def CantidadParadas(self):
        return self._cantidadParadas
    
    def Costo(self):
        return self._costo
    
    def FechaInicio(self, fechaInicio):
        self._fechaInicio = fechaInicio
        
    def FechaFin(self, fechaFin):
        self._fechaFin = fechaFin
    
    def CantidadParadas(self, cantidadParadas):
        self._cantidadParadas = cantidadParadas
        
    def Costo(self, costo):
        self._costo = costo