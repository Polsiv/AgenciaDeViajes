import sys
sys.path.append(r'C:\Users\ACER\Desktop\JD\Semestre_3\Estructura de datos\Semana 18 - Proyecto')
from Clases import pais
import networkx as nx
import matplotlib.pyplot as plt
from Funcionalidades import funcionalidades

#CAMBIAR CANTIDAD DE DIAS Y PRECIOS
rusia = pais.Destino("Rusia", "Moscú", "Hotel Leningrado", 3, 360, ["Visita al Kremlin", "Recorrido por la Plaza Roja"])
china = pais.Destino("China", "Pekin", "The Ritz-Carlton", 4, 600, ["Visita al Kremlin", "Recorrido por la Plaza Roja"])
japon = pais.Destino("Japon", "Tokio", "Hotel Imperial", 4, 600, ["Visita al Templo Senso-ji", "Recorrido por la Torre de Tokio"])
taiwan = pais.Destino("Taiwan", "Taipei", "Hotel Eslite", 2, 240, ["Visita al Palacio Nacional de Taiwán", "Recorrido por Taipei 101"])
tailandia = pais.Destino("Tailandia", "Bangkok", "	Mandarin Oriental", 2, 240, ["Visita al Gran Palacio", "Recorrido por el Templo del Buda Esmeralda"])
arabiaSaudita = pais.Destino("Arabia Saudita", "Riad", "The Ritz-Carlton", 3, 360, ["Visita al Kingdom Centre Tower", "Recorrido por El Murabba Palace,"])
india = pais.Destino("India", "Nueva Delhi", "The Leela Palace", 3, 360, ["Visita al Taj Mahal", "Recorrido por Fuerte Rojo de Delhi"])
indonesia = pais.Destino("Indonesia", "Yakarta", "Hotel Indonesia", 2, 240, ["Visita al Monumento Nacional de Indonesia", "Recorrido por la Isla de Bali"])
coreaDelSur = pais.Destino("Corea del Sur", "Seul", "The Shilla", 4, 600, ["Visita al Palacio Gyeongbokgung", "Recorrido por la Torre de Seúl"])
filipinas = pais.Destino("Filipinas", "Manila", "Okada Manila", 3, 360, ["Visita a Intramuros", "Recorrido por la Bahía de Manila"])

def crearGrafosAsia():
    grafoAsia = nx.Graph()


    grafoAsia.add_edge(rusia, china, costoViaje = 100)

    grafoAsia.add_edge(china, japon, costoViaje = 257)
    grafoAsia.add_edge(china, taiwan, costoViaje = 257)
    grafoAsia.add_edge(china, tailandia, costoViaje = 916)
    grafoAsia.add_edge(china, arabiaSaudita, costoViaje = 295)

    grafoAsia.add_edge(arabiaSaudita, india, costoViaje = 230)

    grafoAsia.add_edge(india, tailandia, costoViaje = 260)
    grafoAsia.add_edge(india, indonesia, costoViaje = 210)

    grafoAsia.add_edge(japon, coreaDelSur, costoViaje = 260)

    grafoAsia.add_edge(taiwan, japon, costoViaje = 260)
    grafoAsia.add_edge(taiwan, india, costoViaje = 260)
    grafoAsia.add_edge(taiwan, filipinas, costoViaje = 260)

    grafoAsia.add_edge(indonesia, japon, costoViaje = 260)
    grafoAsia.add_edge(indonesia, filipinas, costoViaje = 220)
    #------------------------------------------------------------------------------
    
    return grafoAsia

  
asia = crearGrafosAsia()

#funcionalidades.actividadesRuta(asia, china, rusia)
#funcionalidades.caminoMasBarato(asia, china, rusia, True)
#funcionalidades.caminoMasCorto(asia, china, rusia)
#funcionalidades.precioArista(asia, china, filipinas)
funcionalidades.rutasDisponibles(asia, china, rusia)