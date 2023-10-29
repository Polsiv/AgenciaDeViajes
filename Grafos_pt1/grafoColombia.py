import networkx as nx
import matplotlib.pyplot as plt
import pais, funcionalidades

def crearGrafoColombia():
    grafoColombia = nx.Graph()

    grafoColombia.add_edge("Nariño", "Caldas", costoViaje = 100)
    
    grafoColombia.add_edge("Amazonas", "Valle Del Cauca", costoViaje = 100)
    
    grafoColombia.add_edge("Valle Del Cauca", "Cundinamarca", costoViaje = 100)
    grafoColombia.add_edge("Valle Del Cauca", "Caldas", costoViaje = 100)
    
    grafoColombia.add_edge("Cundinamarca", "Santander", costoViaje = 100)
    
    grafoColombia.add_edge("Caldas", "Cundinamarca", costoViaje = 100)
    grafoColombia.add_edge("Caldas", "San Andrés", costoViaje = 100)
    grafoColombia.add_edge("Caldas", "Atlántico", costoViaje = 100)
    grafoColombia.add_edge("Caldas", "Antioquia", costoViaje = 100)
    
    grafoColombia.add_edge("Antioquia", "Magdalena", costoViaje = 100)
    grafoColombia.add_edge("Antioquia", "Cesar", costoViaje = 100)
    
    grafoColombia.add_edge("Santander", "Cesar", costoViaje = 100)
    
    grafoColombia.add_edge("Cesar", "Magdalena", costoViaje = 100)
    
    grafoColombia.add_edge("Magdalena", "Bolívar", costoViaje = 100)
    
    grafoColombia.add_edge("Bolívar", "San Andrés", costoViaje = 100)
    
    #------------------------------------------------------------------------------
    
    return grafoColombia

colombia = crearGrafoColombia()

#funcionalidades.actividadesRuta(colombia, magdalena, antioquia)
#funcionalidades.caminoMasBarato(colombia, magdalena, antioquia, True)
#funcionalidades.caminoMasCorto(colombia, magdalena, antioquia)
#funcionalidades.precioArista(colombia, magdalena, caldas)
funcionalidades.rutasDisponibles(colombia, magdalena, antioquia)