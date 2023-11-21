from tda_tabla_hash import crear_tabla, cantidad_elementos, cantidad_elementos_totales, agregar, buscar_tabla

tabla=crear_tabla(9)
print(tabla)

cantidad=cantidad_elementos(tabla)
print(cantidad)
nombre=input('Ingrese nombre: ')

while(nombre !=''):
    agregar(tabla, nombre)
    nombre=input('Ingrese nombre: ')

print (tabla)
cantidad=cantidad_elementos(tabla)
print("Cantidad posiciones ocupadas: "+str(cantidad))

cantidad_total=cantidad_elementos_totales(tabla)
print("Cantidad total de elementos: "+str(cantidad_total))

buscado=input('Ingrese el nombre a buscar: ')
posicion=buscar_tabla(tabla,buscado)
if (posicion is not None):
    print('Elemento encontrado: ', posicion.info)
else:
    print('No se encontró el elemento buscado')