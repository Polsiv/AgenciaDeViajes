from Graphs import *
from destino import *

grafo = Grafo()
def CrearGrafo(grafo):
    parador_grajales = Destino("Parador Grajales(Valle del Cauca)", False, True,"America", True, False, False, True, True, False, False )
    vina_sicilia = Destino("Viña Sicilia(Antioquia)", False, True,"America", True, False, True, True, True, True, True )
    bodegas_rhin = Destino("Bodegas del Rhin(Cundinamarca)", False, True,"America", True, True, True, True, False, False, False )
    vine_s_morena = Destino("Viñedo Sierra Morena(Santander)", False, True,"America", True, True, False, True, True, False, True )
    vina_aldana = Destino("Viña Aldana(Santander)", False, True,"America", True, False, False, True, True, False, True )
    marques_puntalarga = Destino("Marqués de Puntalarga(Boyaca)", False, True,"America", True, False, False, True, False, False, False )
    vine_ain_karim = Destino("Viñedo Ain Karim(Boyaca)", False, True,"America", True, False, False, True, False, False, False )
    
    insertar_vertice(grafo,vine_s_morena.nombre)
    insertar_vertice(grafo,vina_aldana.nombre )
    insertar_vertice(grafo,marques_puntalarga.nombre)
    insertar_vertice(grafo,vine_ain_karim.nombre)
    insertar_vertice(grafo,parador_grajales.nombre)
    insertar_vertice(grafo,vina_sicilia.nombre)
    insertar_vertice(grafo,bodegas_rhin.nombre)

   
    insertar_arista(grafo, "37/10", parador_grajales.nombre, vina_sicilia.nombre)
    insertar_arista(grafo, "28/11", parador_grajales.nombre, bodegas_rhin.nombre)
    insertar_arista(grafo, "22/2", bodegas_rhin.nombre, vine_ain_karim.nombre)
    insertar_arista(grafo, "17/3", vine_ain_karim.nombre , marques_puntalarga.nombre)
    insertar_arista(grafo, "29/6", vine_ain_karim.nombre , vina_aldana.nombre)
    insertar_arista(grafo, "28/7", marques_puntalarga.nombre, vina_aldana.nombre)
    insertar_arista(grafo, "28/8", marques_puntalarga.nombre, vine_s_morena.nombre)
    insertar_arista(grafo, "18/3", vine_s_morena.nombre, vina_aldana.nombre)
    insertar_arista(grafo, "24/10", vine_s_morena.nombre, vina_sicilia.nombre)
    insertar_arista(grafo, "30/7", vina_sicilia.nombre, bodegas_rhin.nombre)
    insertar_arista(grafo, "32/8", bodegas_rhin.nombre, vine_s_morena.nombre)
#------------------------------------------------------------------------------
    
    
    
    dijkstraCosto(grafo,parador_grajales.nombre,vina_aldana.nombre) 
    dijkstraDistancia(grafo,parador_grajales.nombre,marques_puntalarga.nombre)

    
  
CrearGrafo(grafo) 




