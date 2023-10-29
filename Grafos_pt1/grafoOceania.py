import sys
sys.path.append(r'C:\Users\ACER\Desktop\JD\Semestre_3\Estructura de datos\Semana 18 - Proyecto')
from Clases import pais
import networkx as nx
import matplotlib.pyplot as plt
from Funcionalidades import funcionalidades


australia = pais.Destino("Australia", "Canberra", "Hyatt Hotel", 3, 360, ["Visita a la Bahía de Sidney", "Recorrido por la Gran Barrera de Coral", "Visita a Ayers Rock"])
tonga = pais.Destino("Tonga", "Nukualofa", "Tanoa International Hotel", 2, 220, ["Visita a la Playa Anahulu", "Recorrido por Ha'amonga Maui", "Visita a Talamahu Market"])
nuevaZelanda = pais.Destino("Nueva Zelanda", "Wellington", "InterContinental Wellington", 3, 360, ["Visita al Fiordland National Park", "Recorrido por Milford Sound", "Visita a Waitomo Caves"])
nuevaGuinea = pais.Destino("Nueva Guinea", "Port Moresby", "Airways Hotel", 2, 220, ["Visita al Parque Nacional Varirata", "Recorrido por la Isla de Nueva Bretaña", "Visita al Mercado de Port Moresby"])
marshall = pais.Destino("Marshall", "Majuro", "Marshall Islands Resort", 1, 150, ["Visita al Monumento de la Paz", "Recorrido por la Biblioteca Alele", "Visita a Atolón de Bikini"])
micronesia = pais.Destino("Micronesia", "Palikir", "The Cliff Rainbow Hotel", 1, 150, ["Visita al Parque Nacional de Nan Madol", "Recorrido por la Plaza de la Independencia", " Visita a Lagoon Club"])
solomon = pais.Destino("Solomon", "Honiara", "Heritage Park Hotel", 2, 220, ["Visita al Parque Nacional de la Isla Rennel", "Recorrido por la Playa Bonegi", "Visita a El Abismo"])

def crearGrafosOceania():
    grafoOceania= nx.Graph()
    
    grafoOceania.add_edge(australia, tonga, costoViaje = 100)
    grafoOceania.add_edge(australia, nuevaZelanda, costoViaje = 100)
    grafoOceania.add_edge(australia, nuevaGuinea, costoViaje = 100)
    
    grafoOceania.add_edge(nuevaGuinea, micronesia, costoViaje = 100)
    
    grafoOceania.add_edge(micronesia, marshall, costoViaje = 100)
    grafoOceania.add_edge(micronesia, solomon, costoViaje = 100)
    grafoOceania.add_edge(micronesia, tonga, costoViaje = 100)
    
    grafoOceania.add_edge(tonga, nuevaZelanda, costoViaje = 100)
    
    #------------------------------------------------------------------------------
    
    return grafoOceania

oceania = crearGrafosOceania()

#funcionalidades.actividadesRuta(oceania, tonga, micronesia)
#funcionalidades.caminoMasBarato(oceania, tonga, micronesia, True)
#funcionalidades.caminoMasCorto(oceania, tonga, micronesia)
#funcionalidades.precioArista(oceania, tonga, nuevaZelanda)
funcionalidades.rutasDisponibles(oceania, tonga, micronesia)
funcionalidades.dibujarGrafo(oceania)