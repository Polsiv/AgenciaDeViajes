import networkx as nx
import matplotlib.pyplot as plt
import pais, funcionalidades

# ------------------ instancias de la clase Destino del archivo pais ------------------
colombia = pais.Destino("Colombia", "Bogotá D.C", "Hotel Ibis", 3, 390,   ["Visita al museo del oro", "Visita a monserrate", "Visita Plaza de Bolivar", "Museo Botero"])
venezuela = pais.Destino("Venezuela", "Caracas", "Hotel Cumberland", 3, 260,   ["Visita al panteón nacional", "Visita al parque El Ávila", "Visita Museo Bolivar"])
ecuador = pais.Destino("Ecuador", "Quito", "Adamas House Hotel Boutique", 4, 490,   ["Visita al Parque Nacional Cotopaxi", "Visita a la Mitad del Mundo", "Visita Centro Historico de Quito"])
peru = pais.Destino("Peru", "Lima","Hotel Costa del Sol Wyndham", 3, 360,   ["Visita Plaza Mayor de Lima", "Visita Huaca Pucllana", "Puente de los Suspiros"])
brasil = pais.Destino("Brasil", "Brasilia", "Hotel Royal Tulip Brasília Alvorada", 5, 630,  ["Visita al Palacio de Planalto", "Visita Estadio Mane Garrincha", "Visita Catedral Metropolitana", "Visita Plaza de los Tres Poderes", "Visita Congreso Nacional de Brasil"])
bolivia = pais.Destino("Bolivia", "La Paz", "Hotel Sagarnaga", 3, 310, ["Visita Plaza Metropolitana Murillo", "Visita Valle de la Luna"])
chile = pais.Destino("Chile", "Santiago de Chile", "Hotel Sheraton Santiago Hotel & Convention Center", 4, 520,  ["Visita al Sky Costanera", "Visita Barrio Bellavista", "Visita Parque Bicentenario", "Visita Parque Araucano"])
argentina = pais.Destino("Argentina", "Buenos Aires", "Hotel Gran Hotel Argentino", 5, 610,   ["Visita al Obelisco", "Visita al Jardin Japonez", "Visita Plaza de Mayo","Visita Teatro Colon"])
uruguay = pais.Destino("Uruguay", "Montevideo", "Hotel NH Montevideo Columbia", 3, 400,   ["Visita Teatro Solis", "Visita al Palacio Salvo", "Visita Mercado Agricola de Montevideo"])
panama = pais.Destino("Panama", "Panama City", "Hotel Palmetto Inn & Suites", 4, 600,   ["Visita al St. Andrews State Park", "Visita Panama City Beach", "Visita Pier Park"])
costaRica = pais.Destino("Costa Rica", "San Jose", "Hotel Hilton San Jose La Sabana", 4, 550,   ["Visita al Parque Metropolitano La Sabana", "Visita al Museo de Jade", "Visita al Teatro Nacional"])
republicaDominicana = pais.Destino("Republica Dominicana", "Santo Domingo", "Hotel Catalonia Santo Domingo", 3, 400,   ["Visita al Parque Colon", "Visita al Alcazar de Colon", "Visita a Nuestra Señora de la Encarnacion"])
nicaragua = pais.Destino("Nicaragua","Managua", "Hotel Managua", 2, 280, ["Visita al Museo Nacional", "Exploración del Lago de Managua"])
elSalvador = pais.Destino("El Salvador", "San Salvador", "Hotel San Salvador", 2, 100, ["Visita al Museo de la Palabra y la Imagen", "Paseo por el Parque Cuscatlán"])
guatemala = pais.Destino("Guatemala", "Ciudad de Guatemala", "Hotel Ciudad de Guatemala", 2, 100, ["Exploración de la Zona 10", "Visita al Museo Ixchel"])
cuba = pais.Destino("Cuba", "La Habana", "Hotel La Habana", 3, 300, ["Recorrido por el Malecón", "Visita a la Plaza de la Revolución"])
mexico = pais.Destino("México", "Ciudad de México", "Hotel Ciudad de México", 3, 420, ["Visita al Museo Frida Kahlo", "Paseo por Xochimilco"])
estadosUnidos = pais.Destino("Estados Unidos", "Nueva York", "Hotel Nueva York", 4, 850, ["Exploración de Times Square", "Visita al Museo Metropolitano", "Visita a Central Park", "Visita Estatua de la Libertad"])
canada = pais.Destino("Canadá", "Toronto", "Hotel Toronto", 3, 490, ["Recorrido por la CN Tower", "Visita a las Cataratas del Niágara"])

#Crear el grafo con instancias de paises
def crearGrafosAmerica():
    grafoAmerica = nx.Graph()
    
    grafoAmerica.add_edge(colombia, venezuela, costoViaje = 100)
    grafoAmerica.add_edge(colombia, ecuador, costoViaje = 257)
    grafoAmerica.add_edge(colombia, peru, costoViaje = 257)

    grafoAmerica.add_edge(venezuela, brasil, costoViaje = 216)
    grafoAmerica.add_edge(venezuela, bolivia, costoViaje = 295)

    grafoAmerica.add_edge(ecuador, peru, costoViaje = 230)

    grafoAmerica.add_edge(peru, bolivia, costoViaje = 260)

    grafoAmerica.add_edge(bolivia, brasil, costoViaje = 310)
    grafoAmerica.add_edge(bolivia, chile, costoViaje = 220)

    grafoAmerica.add_edge(brasil, argentina, costoViaje = 270)
    grafoAmerica.add_edge(brasil, uruguay, costoViaje = 220)

    grafoAmerica.add_edge(chile, argentina, costoViaje = 210)

    grafoAmerica.add_edge(argentina, uruguay, costoViaje = 240)
    #------------------------------------------------------------------------------
    grafoAmerica.add_edge(panama, costaRica, costoViaje = 120)
    grafoAmerica.add_edge(panama, republicaDominicana, costoViaje = 405)

    grafoAmerica.add_edge(costaRica, nicaragua, costoViaje = 220)

    grafoAmerica.add_edge(nicaragua, elSalvador, costoViaje = 240)
    grafoAmerica.add_edge(nicaragua, guatemala, costoViaje = 279)
    grafoAmerica.add_edge(nicaragua, cuba, costoViaje = 310)

    grafoAmerica.add_edge(guatemala, cuba, costoViaje = 340)
    grafoAmerica.add_edge(guatemala, mexico, costoViaje = 210)
    
    grafoAmerica.add_edge(cuba, republicaDominicana, costoViaje = 260)

    grafoAmerica.add_edge(republicaDominicana, estadosUnidos, costoViaje = 210)
    grafoAmerica.add_edge(republicaDominicana, canada, costoViaje = 454)

    grafoAmerica.add_edge(mexico, cuba, costoViaje = 310)
    grafoAmerica.add_edge(mexico, estadosUnidos, costoViaje = 360)
    grafoAmerica.add_edge(mexico, canada, costoViaje = 410)

    grafoAmerica.add_edge(estadosUnidos, canada, costoViaje = 240)
    
    #Poner conexiones entre america del sur y del norte
    
    #------------------------------------------------------------------------------
    
    return grafoAmerica

# Crear el grafo
america = crearGrafosAmerica()


#funcionalidades.actividadesRuta(america, colombia, argentina)
#funcionalidades.caminoMasBarato(america, colombia, argentina, True)
#funcionalidades.caminoMasCorto(america, colombia, argentina)
#funcionalidades.precioArista(america, colombia, venezuela)
funcionalidades.rutasDisponibles(america, colombia, argentina)