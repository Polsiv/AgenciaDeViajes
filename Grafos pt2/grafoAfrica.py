import networkx as nx
import matplotlib.pyplot as plt

def crearGrafosAfrica():
    grafoAfrica = nx.Graph()
    

    grafoAfrica.add_edge("Marruecos", "Senegal", costoViaje = 320)
    grafoAfrica.add_edge("Marruecos", "Argelia", costoViaje = 101)
    grafoAfrica.add_edge("Marruecos", "Egipto", costoViaje = 109)
    grafoAfrica.add_edge("Marruecos", "Zimbabue", costoViaje = 100)

    grafoAfrica.add_edge("Egipto", "Argelia", costoViaje = 250)
    grafoAfrica.add_edge("Egipto", "Etiopia", costoViaje = 130)
    grafoAfrica.add_edge("Egipto", "Zimbabue", costoViaje = 200)
    
    grafoAfrica.add_edge("Etiopia", "Kenia", costoViaje = 120)
    grafoAfrica.add_edge("Egipto", "Zimbabue", costoViaje = 160)
    
    grafoAfrica.add_edge("Zimbabue", "Sudafrica", costoViaje = 190)
    
    

 
    #------------------------------------------------------------------------------
    #IMPRIMIR COSTO DE VIAJE EN UNA ARISTA ESPECIFICA
    print(grafoAfrica["Etiopia"]["Kenia"]["costoViaje"])
    
    #IMPRIMIR NODOS EN UN GRAFO
    print(grafoAfrica.nodes)
    
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoAfrica.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoAfrica.nodes:
            destino = str(paisDestino)
            if grafoAfrica.has_edge(origen, destino):
                costo_viaje = grafoAfrica.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    
    #IMPRIMIR EL CAMINO MÁS CORTO ENTRE 2 VERTICES
    inicio = input("- Escriba el origen: ")
    destino = input("- Escriba el destino: ")
    caminoMasCorto = nx.shortest_path(grafoAfrica, inicio, destino)
    print(f"Camino más corto de {inicio} a {destino}: {caminoMasCorto}")
    
    #IMPRIME TODAS LAS RUTAS POSIBLES ENTRE 2 VERTICES
    rutas = list(nx.all_simple_paths(grafoAfrica, inicio, destino))
    print(f"Todas las rutas posibles desde {inicio} a {destino}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
        
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    ruta_mas_economica = nx.dijkstra_path(grafoAfrica, inicio, destino, weight='costoViaje')
    costo_total = nx.dijkstra_path_length(grafoAfrica, inicio, destino, weight='costoViaje')

    print(f"La ruta más económica desde {origen} a {destino}: {ruta_mas_economica}")
    print(f"Costo total del viaje: {costo_total}")
                
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafoAfrica)   
    nx.draw(grafoAfrica, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafoAfrica.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafoAfrica, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()
    
crearGrafosAfrica()