import networkx as nx
import matplotlib.pyplot as plt

def crearGrafosAmerica():
    grafoAmerica = nx.Graph()

    grafoAmerica.add_edge("Colombia", "Venezuela", costoViaje = 100)
    grafoAmerica.add_edge("Colombia", "Ecuador", costoViaje = 257)
    grafoAmerica.add_edge("Colombia", "Perú", costoViaje = 257)

    grafoAmerica.add_edge("Venezuela", "Brasil", costoViaje = 916)
    grafoAmerica.add_edge("Venezuela", "Bolivia", costoViaje = 295)

    grafoAmerica.add_edge("Ecuador", "Perú", costoViaje = 230)

    grafoAmerica.add_edge("Perú", "Bolivia", costoViaje = 260)

    grafoAmerica.add_edge("Bolivia", "Brasil", costoViaje = 310)
    grafoAmerica.add_edge("Bolivia", "Chile", costoViaje = 220)

    grafoAmerica.add_edge("Brasil", "Argentina", costoViaje = 270)
    grafoAmerica.add_edge("Brasil", "Uruguay", costoViaje = 220)

    grafoAmerica.add_edge("Chile", "Argentina", costoViaje = 210)

    grafoAmerica.add_edge("Argentina", "Uruguay", costoViaje = 240)
    #------------------------------------------------------------------------------
    grafoAmerica.add_edge("Panamá", "Costa Rica", costoViaje = 120)
    grafoAmerica.add_edge("Panamá", "República Dominicana", costoViaje = 405)

    grafoAmerica.add_edge("Costa Rica", "Nicaragua", costoViaje = 220)

    grafoAmerica.add_edge("Nicaragua", "El Salvador", costoViaje = 240)
    grafoAmerica.add_edge("Nicaragua", "Guatemala", costoViaje = 279)
    grafoAmerica.add_edge("Nicaragua", "Cuba", costoViaje = 310)

    grafoAmerica.add_edge("Guatemala", "Cuba", costoViaje = 340)
    grafoAmerica.add_edge("Guatemala", "México", costoViaje = 210)

    grafoAmerica.add_edge("Cuba", "República Dominicana", costoViaje = 260)

    grafoAmerica.add_edge("República Dominicana", "Estados Unidos", costoViaje = 210)
    grafoAmerica.add_edge("República Dominicana", "Canadá", costoViaje = 454)

    grafoAmerica.add_edge("México", "Cuba", costoViaje = 310)
    grafoAmerica.add_edge("México", "Estados Unidos", costoViaje = 360)
    grafoAmerica.add_edge("México", "Canadá", costoViaje = 410)

    grafoAmerica.add_edge("Estados Unidos", "Canadá", costoViaje = 240)
    
    #------------------------------------------------------------------------------
    
    #IMPRIMIR COSTO DE VIAJE EN UNA ARISTA ESPECIFICA
    print(grafoAmerica["Argentina"]["Colombia"]["costoViaje"])
    
    #IMPRIMIR NODOS EN UN GRAFO
    print(grafoAmerica.nodes)
    
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoAmerica.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoAmerica.nodes:
            destino = str(paisDestino)
            if grafoAmerica.has_edge(origen, destino):
                costo_viaje = grafoAmerica.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    
    #IMPRIMIR EL CAMINO MÁS CORTO ENTRE 2 VERTICES
    inicio = input("- Escriba el origen: ")
    destino = input("- Escriba el destino: ")
    caminoMasCorto = nx.shortest_path(grafoAmerica, inicio, destino)
    print(f"Camino más corto de {inicio} a {destino}: {caminoMasCorto}")
    
    #IMPRIME TODAS LAS RUTAS POSIBLES ENTRE 2 VERTICES
    rutas = list(nx.all_simple_paths(grafoAmerica, inicio, destino))
    print(f"Todas las rutas posibles desde {inicio} a {destino}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
        
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    ruta_mas_economica = nx.dijkstra_path(grafoAmerica, inicio, destino, weight='costoViaje')
    costo_total = nx.dijkstra_path_length(grafoAmerica, inicio, destino, weight='costoViaje')

    print(f"La ruta más económica desde {origen} a {destino}: {ruta_mas_economica}")
    print(f"Costo total del viaje: {costo_total}")
                
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafoAmerica)   
    nx.draw(grafoAmerica, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafoAmerica.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafoAmerica, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()
    
crearGrafosAmerica()