import networkx as nx
import matplotlib.pyplot as plt
class Messi(object):
    def __init__(self):
        pass
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

#IMPRIMIR COSTO DE VIAJE EN UNA ARISTA ESPECIFICA
    print(grafoOceania["Micronesia"]["Marshall"]["costoViaje"])
    
    #IMPRIMIR NODOS EN UN GRAFO
    print(grafoOceania.nodes)
    
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoOceania.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoOceania.nodes:
            destino = str(paisDestino)
            if grafoOceania.has_edge(origen, destino):
                costo_viaje = grafoOceania.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    
    #IMPRIMIR EL CAMINO MÁS CORTO ENTRE 2 VERTICES
    inicio = input("- Escriba el origen: ")
    destino = input("- Escriba el destino: ")
    caminoMasCorto = nx.shortest_path(grafoOceania, inicio, destino)
    print(f"Camino más corto de {inicio} a {destino}: {caminoMasCorto}")
    
    #IMPRIME TODAS LAS RUTAS POSIBLES ENTRE 2 VERTICES
    rutas = list(nx.all_simple_paths(grafoOceania, inicio, destino))
    print(f"Todas las rutas posibles desde {inicio} a {destino}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
        
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    ruta_mas_economica = nx.dijkstra_path(grafoOceania, inicio, destino, weight='costoViaje')
    costo_total = nx.dijkstra_path_length(grafoOceania, inicio, destino, weight='costoViaje')

    print(f"La ruta más económica desde {origen} a {destino}: {ruta_mas_economica}")
    print(f"Costo total del viaje: {costo_total}")
                
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafoOceania)   
    nx.draw(grafoOceania, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafoOceania.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafoOceania, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()

  
crearGrafosOceania()
