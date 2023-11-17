class Destino(object):
    def __init__(self, nombre,internacional,rutaVino,continente, espanol, bosque, imperial, montana, gastronomia, playa, construcciones):
        self.nombre = nombre #Nombre del destino
        self.internacional=internacional #(true/false)
        self.rutaVino =rutaVino #(true/false)
        self.continente = continente #En que continente se encuentra
        self.espanol = espanol #Si habla español o no (true/false)
        self.bosque = bosque #(true/false)
        self.imperial = imperial #Si el lugar a donde va es imperial (true/false)
        self.montana = montana #(true/false)
        self.gastronomia = gastronomia # Si es conocido por su gastronomia (true/false)
        self.playa = playa  #(true/false)
        self.construcciones = construcciones #Si el lugar es conocido por sus construcciones 
  
        