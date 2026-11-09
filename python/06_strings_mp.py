"""
Manejo de Cadena de Caracteres en Transporte
"""

unidad1 = "Trole-01"
print(f"Unidad1: {unidad1}")
print(f"Tipo de datos: {type(unidad1)}")
unidad2 = "Ecovía-05"
print(f"Unidad2: {unidad2}")
print(f"Tipo de datos: {type(unidad2)}")


######## Funciones comunes de las variables string ########
print("Funciones comunes de texto")
estacion_1 = "Carcelén"
estacion_2 = "Recreo"
longitud_estacion_1 = len(estacion_1)
longitud_estacion_2 = len(estacion_2)
print("Nombre estación 1", estacion_1)
print("Longitud estación 1", longitud_estacion_1)
print("Nombre estación 2", estacion_2)
print("Longitud estación 2", longitud_estacion_2)

print("Convertir mayusculas y minusculas")
mensaje = "la troncal norte conecta con el Labrador"
mensaje_mayuscula = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("mensaje original", mensaje)
print("Mensaje en mayusculas", mensaje_mayuscula)
print("mensaje en minisculas", mensaje_minusculas)

print("Reemplazo de substring")
mensaje = "La unidad viajará a Terminal Sur"
nuevo_mensaje = mensaje.replace("Terminal Sur", "Terminal Carcelén")
print("mensaje original", mensaje)
print("mensaje Reemplazado", nuevo_mensaje)

terminales = "Carcelén,Recreo,Ofelia"
print("terminales: ", terminales)
lista_terminales = terminales.split(",")
print(lista_terminales)
print("Primer terminal: ", lista_terminales[0])

print("Extraer subcadenas")
mensaje = "El corredor norte opera siempre"
corredor = mensaje[3:12]
estado = mensaje[13:19]
print("corredor es: ", corredor)
print("estado es: ", estado)


print("Comprobaciones útiles")
codigo = "TROLE01"
numero = "2026"
nombre = "TransporteUTE"
identificador = "BUSLINEA1"
print(codigo.isalnum())
print(codigo.isdigit())
print(codigo.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())