class Agente(object):
    def __init__(self, usuario, contrasena):
        self._usuario = usuario
        self._contrasena = contrasena
    
    def Usuario(self):
        return self._usuario
    
    def Contrasena(self):
        return self._contrasena
    
    def Usuario(self, usuario):
        self._usuario = usuario
        
    def Contrasena(self, contrasena):
        self._contrasena = contrasena