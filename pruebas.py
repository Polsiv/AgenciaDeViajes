
import networkx as nx
import matplotlib.pyplot as plt
from Clases import agente, planViaje, pais
from Grafos_pt1 import grafoAmerica, grafoEuropa, grafoColombia
#from Grafos_pt2 import grafoAfrica, grafoAsia, grafoOceania

# ------------------ AMERICA ------------------
america = grafoAmerica.crearGrafosAmerica()

# CAMBIAR LA INFORMACION DE CADA INSTANCIA DE ACUERDO AL PAIS (colombia y venezuela listas)
colombia = pais.Destino("Colombia", "Bogotá D.C", "Hotel Ibis", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
venezuela = pais.Destino("Venezuela", "Caracas", "Hotel Cumberland", 3, 80, ["Visita al panteón nacional", "Visita al parque El Ávila"])
# CAMBIAR DE AQUI PARA ABAJO TODA LA INFO (PONER MINIMO 3 ACTIVIDADES)
ecuador = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
peru = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
brasil = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
bolivia = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
chile = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
argentina = pais.Destino("Argentina", "Buenos Aires", "Hotel Obelisco", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
uruguay = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
panama = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
costaRica = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
republicaDominicana = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
nicaragua = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
elSalvador = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
guatemala = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
cuba = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
mexico = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
estadosUnidos = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])
canada = pais.Destino("Colombia", "Bogotá D.C", "Hotel hotelito", 2, 100, ["Visita al museo del oro", "Visita a monserrate"])

if america.has_node(colombia._nombre) and america.has_node(argentina._nombre):
    rutas = list(nx.all_simple_paths(america, colombia._nombre, argentina._nombre))
    print(f"Todas las rutas posibles desde {colombia._nombre} a {argentina._nombre}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
else:
    print("Nao nao")