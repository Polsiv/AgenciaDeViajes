import networkx as nx
import matplotlib.pyplot as plt

def crearGrafosAsia():
    grafoAsia = nx.Graph()


    grafoAsia.add_edge("Rusia", "China", costoViaje = 100)

    grafoAsia.add_edge("China", "Japon", costoViaje = 257)
    grafoAsia.add_edge("China", "Taiwan", costoViaje = 257)
    grafoAsia.add_edge("China", "Tailandia", costoViaje = 916)
    grafoAsia.add_edge("China", "Arabia Saudita", costoViaje = 295)

    grafoAsia.add_edge("Arabia Saudita", "India", costoViaje = 230)

    grafoAsia.add_edge("India", "Tailandia", costoViaje = 260)
    grafoAsia.add_edge("India", "Indonesia", costoViaje = 210)

    grafoAsia.add_edge("Japon", "Corea del Sur ", costoViaje = 260)

    grafoAsia.add_edge("Taiwan", "Japon", costoViaje = 260)
    grafoAsia.add_edge("Taiwan", "India", costoViaje = 260)
    grafoAsia.add_edge("Taiwan", "Filipinas", costoViaje = 260)

    grafoAsia.add_edge("Indonesia", "Japon", costoViaje = 260)
    grafoAsia.add_edge("Indonesia", "Filipinas", costoViaje = 220)




 
    #------------------------------------------------------------------------------


   #IMPRIMIR COSTO DE VIAJE EN UNA ARISTA ESPECIFICA
    print(grafoAsia["India"]["Indonesia"]["costoViaje"])
    
    #IMPRIMIR NODOS EN UN GRAFO
    print(grafoAsia.nodes)
    
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoAsia.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoAsia.nodes:
            destino = str(paisDestino)
            if grafoAsia.has_edge(origen, destino):
                costo_viaje = grafoAsia.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    
    #IMPRIMIR EL CAMINO MÁS CORTO ENTRE 2 VERTICES
    inicio = input("- Escriba el origen: ")
    destino = input("- Escriba el destino: ")
    caminoMasCorto = nx.shortest_path(grafoAsia, inicio, destino)
    print(f"Camino más corto de {inicio} a {destino}: {caminoMasCorto}")
    
    #IMPRIME TODAS LAS RUTAS POSIBLES ENTRE 2 VERTICES
    rutas = list(nx.all_simple_paths(grafoAsia, inicio, destino))
    print(f"Todas las rutas posibles desde {inicio} a {destino}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
        
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    ruta_mas_economica = nx.dijkstra_path(grafoAsia, inicio, destino, weight='costoViaje')
    costo_total = nx.dijkstra_path_length(grafoAsia, inicio, destino, weight='costoViaje')

    print(f"La ruta más económica desde {origen} a {destino}: {ruta_mas_economica}")
    print(f"Costo total del viaje: {costo_total}")
                
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafoAsia)   
    nx.draw(grafoAsia, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafoAsia.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafoAsia, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()
    

  
crearGrafosAsia()