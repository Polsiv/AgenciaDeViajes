import networkx as nx
import matplotlib.pyplot as plt

#Dibujar el grafo por medio de la libreria matplotlib.pyplot
def dibujarGrafo(grafo):
    #DIBUJAR GRAFO
    posUno = nx.spring_layout(grafo)   
    nx.draw(grafo, posUno, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_color="black")
    
    # Obtener las etiquetas de peso de las aristas
    edge_labels = {(u, v): d['costoViaje'] for u, v, d in grafo.edges(data=True)}

    # Dibujar las etiquetas de peso en el gráfico
    nx.draw_networkx_edge_labels(grafo, posUno, edge_labels=edge_labels, font_size=10)
    
    # MOSTRAR GRAFO
    plt.show()

def rutasDisponibles(grafo, origen, destino):

    if grafo.has_node(origen) and grafo.has_node(destino):
        contador = 1
        rutas = list(nx.all_simple_paths(grafo, origen, destino))
        print(f"Todas las rutas posibles desde {origen._nombre} a {destino._nombre}:")
        for ruta in rutas:
            precioRuta = 0
            impresionRuta = ""
            for i in range (len(ruta)):
                impresionRuta += ruta[i]._nombre + ", "
                if i < (len(ruta)-1):
                    precioRuta += grafo[ruta[i]][ruta[i+1]]["costoViaje"]
            print("Ruta ", contador, ": " + impresionRuta + " - $" + str(precioRuta))
            contador += 1
    else:
        print("nao nao")
        
def precioArista(grafo, origen, destino):
    print("El precio del viaje de ", origen._nombre, " a ", destino._nombre, " es de $",grafo[origen][destino]["costoViaje"])
    
    """
    #IMPRIMIR PESO DE CADA ARISTA
    for paisOrigen in grafoAmerica.nodes:
        origen = str(paisOrigen)
        for paisDestino in grafoAmerica.nodes:
            destino = str(paisDestino)
            if grafoAmerica.has_edge(origen, destino):
                costo_viaje = grafoAmerica.get_edge_data(origen, destino)["costoViaje"]
                print(f"Costo de viaje desde {origen} a {destino}: {costo_viaje}")
    """
    
def caminoMasCorto(grafo, origen, destino):
    caminoMasCorto = nx.shortest_path(grafo, origen, destino)
    impresionCamino = ""

    for i in range (0, len(caminoMasCorto)):
        impresionCamino += caminoMasCorto[i]._nombre + ", "
        
    print(f"Camino más corto de {origen._nombre} a {destino._nombre}: {impresionCamino}")

def caminoMasBarato(grafo, origen, destino, imprimir:bool):
    #IMPRIME LA RUTA MÁS ECONÓMICA ENTRE 2 VERTICES Y EL COSTO TOTAL DEL VIAJE
    rutaMasEconomica = nx.dijkstra_path(grafo, origen, destino, weight='costoViaje')
    costoTotal = nx.dijkstra_path_length(grafo, origen, destino, weight='costoViaje')
    impresionCamino = ""

    for i in range (0, len(rutaMasEconomica)):
        impresionCamino += rutaMasEconomica[i]._nombre + ", "
    if imprimir is True:
        print(f"La ruta más económica desde {origen._nombre} a {destino._nombre}: {impresionCamino}")
        print(f"Costo total del viaje: ${costoTotal}")
    return rutaMasEconomica, costoTotal
    
def actividadesRuta(grafo, origen, destino):
    ruta, costoViaje = caminoMasBarato(grafo, origen, destino, False)
    precioTotalActividades = 0
    precioTotalPlanViaje = 0
    for pais in ruta:
        print("En ", pais._nombre, " tienes disponibles las siguientes actividades: ")
        for i in range (0, len(pais._listaActividades)):
            print((i+1), " - ", pais._listaActividades[i])
        precioTotalActividades += pais._costo
        #actividades.append(pais._listaActividades)
    precioTotalPlanViaje += costoViaje + precioTotalActividades
    
    print("El costo total del plan de viaje es de $", precioTotalPlanViaje)
        