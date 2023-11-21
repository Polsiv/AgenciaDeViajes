from tda_tabla_hash import *
from Cliente import Cliente


cliente1 = Cliente("Pepe", "Camelot", "pepe@correo.com", "32384131", "82733671201")
cliente2 = Cliente("Pepe1", "Camelot1", "pepe1@correo.com", "32183131", "47438344334")
cliente2 = Cliente("Pepe2", "Camelot2", "pepe2@correo.com", "18836715", "84575132937")

class Agente(object):
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password


agente1 = Agente("Julia Pinneda", "julia123")
agente2 = Agente("ProgramadorJunior", "programador123")

tabla = crear_tabla(5)

agregar(tabla, agente1)
agregar(tabla, agente2)

print(buscar_tabla(tabla, agente1.usuario))