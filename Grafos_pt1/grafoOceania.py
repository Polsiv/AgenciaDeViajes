import networkx as nx
import matplotlib.pyplot as plt
import pais, funcionalidades


def crearGrafosOceania():
    grafoOceania= nx.Graph()
    
    grafoOceania.add_edge("Australia", "Tonga", costoViaje = 100)
    grafoOceania.add_edge("Australia", "Nueva Zelanda", costoViaje = 100)
    grafoOceania.add_edge("Australia", "Nueva Guinea", costoViaje = 100)
    
    grafoOceania.add_edge("Nueva Guinea", "Micronesia", costoViaje = 100)
    
    grafoOceania.add_edge("Micronesia", "Marshall", costoViaje = 100)
    grafoOceania.add_edge("Micronesia", "Solomon", costoViaje = 100)
    grafoOceania.add_edge("Micronesia", "Tonga", costoViaje = 100)
    
    grafoOceania.add_edge("Tonga", "Nueva Zelanda", costoViaje = 100)
    
    #------------------------------------------------------------------------------
    
    return grafoOceania

oceania = crearGrafosOceania()

#funcionalidades.actividadesRuta(oceania, tonga, micronesia)
#funcionalidades.caminoMasBarato(oceania, tonga, micronesia, True)
#funcionalidades.caminoMasCorto(oceania, tonga, micronesia)
#funcionalidades.precioArista(oceania, tonga, solomon)
funcionalidades.rutasDisponibles(oceania, tonga, micronesia)