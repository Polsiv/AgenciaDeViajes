import sys
sys.path.append(r'C:\Users\ACER\Desktop\JD\Semestre_3\Estructura de datos\Semana 18 - Proyecto')
from Clases import pais
import networkx as nx
import matplotlib.pyplot as plt
from Funcionalidades import funcionalidades


narino = pais.Destino("Nariño", "Pasto", "Hotel Nariño", 2, 80, ["Visita a La Catedral Basílica de Pasto", "Visita a La Laguna de la Cocha", "Visita al Parque Nariño"])
caldas = pais.Destino("Caldas", "Manizales", "Hotel Termales del Ruiz", 2, 80,   ["Visita a la Catedral Basílica de Manizales", "Visita al Parque Natural de Los Nevados", "Visita al Palacio de Bellas Artes"])
amazonas = pais.Destino("Amazonas", "Leticia", "Hotel Waira Suites", 3, 250,   ["Visita a la Reserva Nacional Natural Cahuinari", "Visita al Parque Santander", "Visita al Mirador de Santa Rita"])
valleDelCauca = pais.Destino("Valle Del Cauca", "Cali", "Hotel InterContinental", 3, 400,   ["Visita a Cristo Rey", "Visita a Gato de Tejada", "Visita al Zoológico de Cali"])
cundinamarca = pais.Destino("Cundinamarca", "Bogotá D.C", "Hotel JW Marriott Bogotá", 3, 450,   ["Visita al museo del oro", "Visita a monserrate", "Visita Plaza de Bolivar"])
santander = pais.Destino("Santander", "Bucaramanga", "Hotel Chicamocha by Sercotel", 2, 120,   ["Visita al Parque Nacional del Chicamocha", "Visita a la Catedral de la Sagrada Familia", "Visita al Parque Santander"])
sanAndres = pais.Destino("San Andres", "San Andres", "Decameron San Luis", 2, 200,   ["Visita al Hoyo Soplador", "Visita a la Playa de San Luis", "Visita al Parque Johnny Cay"])
atlantico = pais.Destino("Atlantico", "Barranquilla", "Dann Carlton Hotel", 2, 120,   ["Visita al Museo del Caribe", "Visita al Castillo de Salgar", "Visita al Parque Venezuela"])
antioquia = pais.Destino("Antioquia", "Medellin", "Hotel Dann Carlton Medellín", 3, 420,   ["Visita al Parque Arvi", "Visita al Jardín Botánico de Medellín", "Visita al Museo de Antioquia"])
magdalena = pais.Destino("Magdalena", "Santa Marta", "Irotama Resort", 3, 350,   ["Visita al Parque Nacional Natural Tayrona", "Visita a Playa Blanca", "Visita a la Catedral Basílica de Santa Marta"])
cesar = pais.Destino("Cesar", "Valledupar", "Hotel Sicarare", 2, 120,   ["Visita al Parque de la Leyenda Vallenata", "Visita a la Plaza Alfonso López", "Visita a la Iglesia de Santo Ecce Homo"])
bolivar = pais.Destino("Bolivar", "Cartagena", "Hotel Sofitel Legend Santa Clara", 3, 350,   ["Visita al Castillo San Felipe de Barajas", "Visita a Playa Blanca", "Visita a la Ciudad Amurallada"])

def crearGrafoColombia():
    
    grafoColombia = nx.Graph()

    grafoColombia.add_edge(narino, caldas, costoViaje = 54)
    
    grafoColombia.add_edge(amazonas, valleDelCauca, costoViaje = 63)
    
    grafoColombia.add_edge(valleDelCauca, cundinamarca, costoViaje = 54)
    grafoColombia.add_edge(valleDelCauca, caldas, costoViaje = 58)
    
    grafoColombia.add_edge(cundinamarca, santander, costoViaje = 54)
    
    grafoColombia.add_edge(caldas, cundinamarca, costoViaje = 58)
    grafoColombia.add_edge(caldas, sanAndres, costoViaje = 58)
    grafoColombia.add_edge(caldas, atlantico, costoViaje = 58)
    grafoColombia.add_edge(caldas, antioquia, costoViaje = 58)
    
    grafoColombia.add_edge(antioquia, magdalena, costoViaje = 58)
    grafoColombia.add_edge(antioquia, cesar, costoViaje = 78)
    
    grafoColombia.add_edge(santander, cesar, costoViaje = 153)
    
    grafoColombia.add_edge(cesar, magdalena, costoViaje = 160)
    
    grafoColombia.add_edge(magdalena, bolivar, costoViaje = 58)
    
    grafoColombia.add_edge(bolivar, sanAndres, costoViaje = 63)
    
    #------------------------------------------------------------------------------
    
    return grafoColombia

colombia = crearGrafoColombia()

#funcionalidades.actividadesRuta(colombia, magdalena, antioquia)
#funcionalidades.caminoMasBarato(colombia, magdalena, antioquia, True)
#funcionalidades.caminoMasCorto(colombia, magdalena, antioquia)
#funcionalidades.precioArista(colombia, magdalena, caldas)
funcionalidades.rutasDisponibles(colombia, magdalena, antioquia)
funcionalidades.dibujarGrafo(colombia)