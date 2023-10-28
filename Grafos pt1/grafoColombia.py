import networkx as nx
import matplotlib.pyplot as plt

def crearGrafoColombia():
    grafoColombia = nx.Graph()

    grafoColombia.add_edge("Nariño", "Caldas", costoViaje = 100)
    
    grafoColombia.add_edge("Amazonas", "Valle Del Cauca", costoViaje = 100)
    
    grafoColombia.add_edge("Valle Del Cauca", "Cundinamarca", costoViaje = 100)
    grafoColombia.add_edge("Valle Del Cauca", "Caldas", costoViaje = 100)
    
    grafoColombia.add_edge("Cundinamarca", "Santander", costoViaje = 100)
    
    grafoColombia.add_edge("Caldas", "Cundinamarca", costoViaje = 100)
    grafoColombia.add_edge("Caldas", "San Andrés", costoViaje = 100)
    grafoColombia.add_edge("Caldas", "Atlántico", costoViaje = 100)
    grafoColombia.add_edge("Caldas", "Antioquia", costoViaje = 100)
    
    grafoColombia.add_edge("Antioquia", "Magdalena", costoViaje = 100)
    grafoColombia.add_edge("Antioquia", "Cesar", costoViaje = 100)
    
    grafoColombia.add_edge("Santander", "Cesar", costoViaje = 100)
    
    grafoColombia.add_edge("Cesar", "Magdalena", costoViaje = 100)
    
    grafoColombia.add_edge("Magdalena", "Bolívar", costoViaje = 100)
    
    grafoColombia.add_edge("Bolívar", "San Andrés", costoViaje = 100)
    
    #------------------------------------------------------------------------------
    
    #IMPRIMIR COSTO DE VIAJE EN UNA ARISTA ESPECIFICA
    print(grafoColombia["Bolívar"]["San Andrés"]["costoViaje"])
    
    #IMPRIMIR NODOS EN UN GRAFO
    print(grafoColombia.nodes)
    
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoColombia.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoColombia.nodes:
            destino = str(paisDestino)
            if grafoColombia.has_edge(origen, destino):
                costo_viaje = grafoColombia.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    
    #IMPRIMIR EL CAMINO MÁS CORTO ENTRE 2 VERTICES
    inicio = input("- Escriba el origen: ")
    destino = input("- Escriba el destino: ")
    caminoMasCorto = nx.shortest_path(grafoColombia, inicio, destino)
    print(f"Camino más corto de {inicio} a {destino}: {caminoMasCorto}")
    
    #IMPRIME TODAS LAS RUTAS POSIBLES ENTRE 2 VERTICES
    rutas = list(nx.all_simple_paths(grafoColombia, inicio, destino))
    print(f"Todas las rutas posibles desde {inicio} a {destino}:")
    for i, ruta in enumerate(rutas, start=1):
        print(f"Ruta {i}: {ruta}")
        
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    ruta_mas_economica = nx.dijkstra_path(grafoColombia, inicio, destino, weight='costoViaje')
    costo_total = nx.dijkstra_path_length(grafoColombia, inicio, destino, weight='costoViaje')

    print(f"La ruta más económica desde {origen} a {destino}: {ruta_mas_economica}")
    print(f"Costo total del viaje: {costo_total}")
                
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafoColombia)   
    nx.draw(grafoColombia, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafoColombia.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafoColombia, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()
    
crearGrafoColombia()