import networkx as nx
import matplotlib.pyplot as plt

def crearGrafosEuropa():
    grafoEuropa = nx.Graph()

    grafoEuropa.add_edge("España", "Portugal", costoViaje = 100)
    grafoEuropa.add_edge("España", "Grecia", costoViaje = 100)
    grafoEuropa.add_edge("España", "Francia", costoViaje = 100)
    grafoEuropa.add_edge("España", "Italia", costoViaje = 100)
    
    grafoEuropa.add_edge("Portugal", "Inglaterra", costoViaje = 100)
    grafoEuropa.add_edge("Portugal", "Noruega", costoViaje = 100)
    grafoEuropa.add_edge("Portugal", "Bélgica", costoViaje = 100)
    
    grafoEuropa.add_edge("Inglaterra", "Islandia", costoViaje = 100)
    grafoEuropa.add_edge("Inglaterra", "Rusia", costoViaje = 100)
    grafoEuropa.add_edge("Inglaterra", "Noruega", costoViaje = 100)
    
    grafoEuropa.add_edge("Noruega", "Paises Bajos", costoViaje = 100)
    grafoEuropa.add_edge("Noruega", "Alemania", costoViaje = 100)
    grafoEuropa.add_edge("Noruega", "Suecia", costoViaje = 100)
    grafoEuropa.add_edge("Noruega", "Bielorrusia", costoViaje = 100)
    
    grafoEuropa.add_edge("Francia", "Italia", costoViaje = 100)
    grafoEuropa.add_edge("Francia", "Alemania", costoViaje = 100)
    
    grafoEuropa.add_edge("Italia", "Alemania", costoViaje = 100)
    
    grafoEuropa.add_edge("Grecia", "Turquía", costoViaje = 100)
    grafoEuropa.add_edge("Grecia", "Serbia", costoViaje = 100)
    grafoEuropa.add_edge("Grecia", "Bulgaria", costoViaje = 100)
    
    grafoEuropa.add_edge("Turquía", "Bulgaria", costoViaje = 100)
    grafoEuropa.add_edge("Turquía", "Ucrania", costoViaje = 100)
    
    grafoEuropa.add_edge("Bulgaria", "Serbia", costoViaje = 100)
    grafoEuropa.add_edge("Bulgaria", "Romania", costoViaje = 100)
    grafoEuropa.add_edge("Bulgaria", "Ucrania", costoViaje = 100)
    
    grafoEuropa.add_edge("Ucrania", "Bielorrusia", costoViaje = 100)
    
    grafoEuropa.add_edge("Suecia", "Alemania", costoViaje = 100)
    grafoEuropa.add_edge("Suecia", "Bielorrusia", costoViaje = 100)
    
    grafoEuropa.add_edge("Alemania", "Bélgica", costoViaje = 100)
    grafoEuropa.add_edge("Alemania", "Paises Bajos", costoViaje = 100)
    grafoEuropa.add_edge("Alemania", "Romania", costoViaje = 100)
    grafoEuropa.add_edge("Alemania", "Bielorrusia", costoViaje = 100)
    
    grafoEuropa.add_edge("Rusia", "Inglaterra", costoViaje = 100)
    grafoEuropa.add_edge("Rusia", "Noruega", costoViaje = 100)
    
    #------------------------------------------------------------------------------
    
    #IMPRIMIR COSTO DE VIAJE EN UNA ARISTA ESPECIFICA
    print(grafoEuropa["Rusia"]["Alemania"]["costoViaje"])
    
    #IMPRIMIR NODOS EN UN GRAFO
    print(grafoEuropa.nodes)
    
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoEuropa.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoEuropa.nodes:
            destino = str(paisDestino)
            if grafoEuropa.has_edge(origen, destino):
                costo_viaje = grafoEuropa.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    
    #IMPRIMIR EL CAMINO MÁS CORTO ENTRE 2 VERTICES
    inicio = input("- Escriba el origen: ")
    destino = input("- Escriba el destino: ")
    caminoMasCorto = nx.shortest_path(grafoEuropa, inicio, destino)
    print(f"Camino más corto de {inicio} a {destino}: {caminoMasCorto}")
    
    #IMPRIME TODAS LAS RUTAS POSIBLES ENTRE 2 VERTICES
    rutas = list(nx.all_simple_paths(grafoEuropa, inicio, destino))
    print(f"Todas las rutas posibles desde {inicio} a {destino}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
        
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    ruta_mas_economica = nx.dijkstra_path(grafoEuropa, inicio, destino, weight='costoViaje')
    costo_total = nx.dijkstra_path_length(grafoEuropa, inicio, destino, weight='costoViaje')

    print(f"La ruta más económica desde {origen} a {destino}: {ruta_mas_economica}")
    print(f"Costo total del viaje: {costo_total}")
                
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafoEuropa)   
    nx.draw(grafoEuropa, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafoEuropa.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafoEuropa, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()
    
crearGrafosEuropa()