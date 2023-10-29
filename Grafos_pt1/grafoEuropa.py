import sys
sys.path.append(r'C:\Users\ACER\Desktop\JD\Semestre_3\Estructura de datos\Semana 18 - Proyecto')
from Clases import pais
import networkx as nx
import matplotlib.pyplot as plt
from Funcionalidades import funcionalidades

espana = pais.Destino("España", "Madrid", "Avani Alonso Martínez Madrid Hotel", 3, 570, ["Visita al Museo del Prado", "Tour por el Palacio Real", "Parque de El Retiro"])
portugal = pais.Destino("Portugal", "Lisboa", "Hotel Tivoli Avenida Liberdade Lisboa", 3, 410, ["Exploración de la Torre de Belém", "Visita al Barrio Alto", "Visita Catedral de Lisboa"])
reinoUnido = pais.Destino("Inglaterra", "Londres", "Hotel Zedwell Piccadilly Circus", 4, 620, ["Visita al Palacio de Buckingham", "Paseo por el Museo Británico", "Visita Torre de Londres", "Visita Puente de la Torre"])
noruega = pais.Destino("Noruega", "Oslo", "Hotel Citybox Oslo", 3, 490, ["Exploración del Museo Munch", "Paseo por el Parque Vigeland", "Visita Parque Frogner"])
paisesBajos= pais.Destino("Países Bajos", "Ámsterdam", "Hotel YOTEL Amsterdam", 3, 340, ["Recorrido en barco por los canales", "Visita al Museo Van Gogh"])
belgica = pais.Destino("Belgica", "Bruselas", "Hotel Appart'City Confort Bruxelles Centre Gare du Midi", 2, 420, ["Visita a la Grand Place", "Exploración del Atomium"])
islandia = pais.Destino("Islandia", "Reikiavik", "Hotel ODDSSON Hotel", 4, 410, ["Excursión a las Cascadas Gullfoss", "Visita a la Laguna Azul"])
rusia = pais.Destino("Rusia", "Moscú", "Hotel Leningrado", 5, 650, ["Visita al Kremlin", "Recorrido por la Plaza Roja"])
alemania = pais.Destino("Alemania", "Berlín", "Novum Hotel City B Berlin Centrum", 3, 410, ["Visita al Muro de Berlín", "Exploración de la Puerta de Brandeburgo"])
suecia = pais.Destino("Suecia", "Estocolmo", "Hotel Hilton Stockholm Slussen", 3, 330, ["Paseo por el Casco Antiguo de Gamla Stan", "Visita al Museo ABBA"])
bielorrusia = pais.Destino("Bielorrusia", "Minsk", "Minsk Hotel", 2, 400, ["Exploración de la Plaza de la Independencia", "Visita al Museo Nacional de Historia"])
francia = pais.Destino("Francia", "París", "Virginia Hotel", 4, 550, ["Visita a la Torre Eiffel", "Recorrido por el Museo del Louvre"])
italia = pais.Destino("Italia", "Roma", "Hotel Roma Tor Vergata", 5, 850, ["Visita al Coliseo", "Exploración del Vaticano"])
grecia = pais.Destino("Grecia", "Atenas", "Arion Athens Hotel", 3, 420, ["Visita al Partenón", "Exploración de la Acrópolis"])
turquia = pais.Destino("Turquia","Ankara", "Anatolia Luxury Hotel", 4, 470, ["Visita al Mausoleo de Atatürk", "Recorrido por el Museo de las Civilizaciones de Anatolia"])
serbia = pais.Destino("Serbia", "Belgrado", "Hotel Belgrado", 2, 380, ["Paseo por la Fortaleza de Belgrado", "Visita a la Catedral de San Sava"])
bulgaria = pais.Destino("Bulgaria", "Sofía", "Hotel LION Sofia", 2, 340, ["Exploración de la Catedral de San Alejandro Nevski", "Visita al Museo Nacional de Historia Militar"])
ucrania = pais.Destino("Ucrania", "Kiev", "Hotel Hilton Kyiv", 3, 420, ["Visita al Monasterio de las Cuevas de Kiev", "Paseo por la Plaza de la Independencia"])
rumania = pais.Destino("Rumania", "Bucarest", "Hotel Hilton Garden Inn Bucharest Old Town", 3, 460, ["Exploración del Palacio del Parlamento", "Visita al Museo del Pueblo Rumano"])

#Crear el grafo con instancias de paises
def crearGrafosEuropa():
    grafoEuropa = nx.Graph()

    grafoEuropa.add_edge(espana, portugal, costoViaje = 100)
    grafoEuropa.add_edge(espana, grecia, costoViaje = 220)
    grafoEuropa.add_edge(espana, francia, costoViaje = 90)
    grafoEuropa.add_edge(espana, italia, costoViaje = 230)
    
    grafoEuropa.add_edge(portugal, reinoUnido, costoViaje = 250)
    grafoEuropa.add_edge(portugal, noruega, costoViaje = 340)
    grafoEuropa.add_edge(portugal, belgica, costoViaje = 160)
    
    grafoEuropa.add_edge(reinoUnido, islandia, costoViaje = 210)
    grafoEuropa.add_edge(reinoUnido, rusia, costoViaje = 380)
    grafoEuropa.add_edge(reinoUnido, noruega, costoViaje = 270)
    
    grafoEuropa.add_edge(noruega, paisesBajos, costoViaje = 210)
    grafoEuropa.add_edge(noruega, alemania, costoViaje = 210)
    grafoEuropa.add_edge(noruega, suecia, costoViaje = 170)
    grafoEuropa.add_edge(noruega, bielorrusia, costoViaje = 250)
    
    grafoEuropa.add_edge(francia, italia, costoViaje = 180)
    grafoEuropa.add_edge(francia, alemania, costoViaje = 150)
    
    grafoEuropa.add_edge(italia, alemania, costoViaje = 200)
    
    grafoEuropa.add_edge(grecia, turquia, costoViaje = 120)
    grafoEuropa.add_edge(grecia, serbia, costoViaje = 110)
    grafoEuropa.add_edge(grecia, bulgaria, costoViaje = 100)
    
    grafoEuropa.add_edge(turquia, bulgaria, costoViaje = 110)
    grafoEuropa.add_edge(turquia, ucrania, costoViaje = 220)
    
    grafoEuropa.add_edge(bulgaria, serbia, costoViaje = 70)
    grafoEuropa.add_edge(bulgaria, rumania, costoViaje = 60)
    grafoEuropa.add_edge(bulgaria, ucrania, costoViaje = 180)
    
    grafoEuropa.add_edge(ucrania, bielorrusia, costoViaje = 140)
    
    grafoEuropa.add_edge(suecia, alemania, costoViaje = 130)
    grafoEuropa.add_edge(suecia, bielorrusia, costoViaje = 250)
    
    grafoEuropa.add_edge(alemania, belgica, costoViaje = 80)
    grafoEuropa.add_edge(alemania, paisesBajos, costoViaje = 90)
    grafoEuropa.add_edge(alemania, rumania, costoViaje = 170)
    grafoEuropa.add_edge(alemania, bielorrusia, costoViaje = 200)
    
    grafoEuropa.add_edge(rusia, reinoUnido, costoViaje = 350)
    grafoEuropa.add_edge(rusia, noruega, costoViaje = 300)
    
    #------------------------------------------------------------------------------
    
    return grafoEuropa

europa = crearGrafosEuropa()

#funcionalidades.actividadesRuta(europa, alemania, rusia)
#funcionalidades.caminoMasBarato(europa, alemania, rusia, True)
#funcionalidades.caminoMasCorto(europa, alemania, rusia)
#funcionalidades.precioArista(europa, alemania, belgica)
funcionalidades.rutasDisponibles(europa, alemania, rusia)