import sys
sys.path.append(r'C:\Users\ACER\Desktop\JD\Semestre_3\Estructura de datos\Semana 18 - Proyecto')
from Clases import pais
import networkx as nx
import matplotlib.pyplot as plt
from Funcionalidades import funcionalidades

senegal = pais.Destino("Senegal", "Dakar", "Radisson Blu Hotel, Dakar Sea Plaza", 2, 490, ["Exploración de la Isla de Gorée", "Visita al Monumento del Renacimiento Africano", "Paseo por la playa de Dakar"])
argelia = pais.Destino("Argelia", "Argel", "ibis Alger Aéroport", 3, 460, ["Visita a la Casbah de Argel", "Paseo por la Plaza de la Grande Poste", "Exploración del Jardín de Essai"])
egipto = pais.Destino("Egipto", "El Cairo", "Novotel Cairo Airport", 4, 750, ["Visita a las Pirámides de Giza", "Recorrido por el Museo Egipcio", "Navegación por el Nilo"])
zimbabue = pais.Destino("Zimbabue", "Harare", "The Rainbow Towers Hotel and Conference", 2, 480, ["Exploración del Parque Nacional de Mukuvisi", "Visita al Museo Nacional de Zimbabue", "Paseo por el Lago Chivero"])
etiopia = pais.Destino("Etiopia","Addis Abeba", "Harmony Hotel", 3, 520, ["Recorrido por la Iglesia de San Jorge", "Visita al Museo Nacional de Etiopía", "Paseo por el Mercato"])
kenia = pais.Destino("Kenia", "Nairobi", "ibis Styles Nairobi Westlands", 3, 530, ["Safari en el Parque Nacional de Nairobi", "Visita al Museo Karen Blixen", "Paseo por el Parque Nacional de Hell's Gate"])
sudafrica = pais.Destino("Sudafrica", "Ciudad del Cabo", "Grande Kloof Boutique Hotel", 4, 780, ["Ascenso a la Montaña de la Mesa", "Recorrido por la Península del Cabo", "Visita a la Isla Robben"])
marruecos = pais.Destino("Marruecos", "Ranat", " The View Luxury Resort", 4, 780, ["Visita a Kasbah des Oudaias", "Recorrido por Mausoleo de Mohamed V"])

def crearGrafosAfrica():
    grafoAfrica = nx.Graph()
    
    grafoAfrica.add_edge(marruecos, senegal, costoViaje = 320)
    grafoAfrica.add_edge(marruecos, argelia, costoViaje = 101)
    grafoAfrica.add_edge(marruecos, egipto, costoViaje = 109)
    grafoAfrica.add_edge(marruecos, zimbabue, costoViaje = 100)

    grafoAfrica.add_edge(egipto, argelia, costoViaje = 250)
    grafoAfrica.add_edge(egipto, etiopia, costoViaje = 130)
    grafoAfrica.add_edge(egipto, zimbabue, costoViaje = 200)
    
    grafoAfrica.add_edge(etiopia, kenia, costoViaje = 120)
    grafoAfrica.add_edge(egipto, zimbabue, costoViaje = 160)
    
    grafoAfrica.add_edge(zimbabue, sudafrica, costoViaje = 190)
    
    #------------------------------------------------------------------------------
    
    return grafoAfrica
africa = crearGrafosAfrica()

#funcionalidades.actividadesRuta(africa, egipto, sudafrica)
#funcionalidades.caminoMasBarato(africa, egipto, sudafrica, True)
#funcionalidades.caminoMasCorto(africa, egipto, sudafrica)
#funcionalidades.precioArista(africa, egipto, marruecos)
funcionalidades.rutasDisponibles(africa, egipto, sudafrica)