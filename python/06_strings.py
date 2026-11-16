"""
Manejo de Cadena de Carcteres
"""

nombre1="Qui-Gon-Jin"
print(f"Jedi1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")
nombre2="Obiwan Kenobi"
print(f"Jedi2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")


######## Funciones comunes de las variables string ########
print("Funciones comunes de texto")
droide_1 = "R2-D2"
droide_2 = "C3PO"
longitud_droide_1 = len(droide_1)
longitud_droide_2 = len(droide_2)
print("Nombre droide 1", droide_1)
print("Longitud droide 1", longitud_droide_1 )
print("Nombre droide 2", droide_2)
print("Longitud droide 2", longitud_droide_2 )

print("Convertir mayusculas y minusculas")
mensaje = "La federecion invade al Planeta Naboo"
mensaje_mayuscula = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("mensaje original", mensaje)
print("Mensaje en mayusculas", mensaje_mayuscula)
print("mensaje en minisculas", mensaje_minusculas)

print("Reemplazo de substring")
mensaje = "La nave viajara a tatooine"
nuevo_mensaje = mensaje.replace("tatooine","Coruscant")
print("mensaje  original", mensaje)
print("mensaje Reemplazado", nuevo_mensaje)

planetas = "Naboo,Tatooine,Kmino"
print("planetas: ", planetas)
lista_planetas= planetas.split(",")
print(lista_planetas)
print("Primer planeta: ", lista_planetas[0])

print("Extraer subacadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[7:13]
verbo = mensaje[17:25]
print("adjetivo es: ", adjetivo)
print("verbio es: ", verbo)


print("COmprobaciones útiles")
codigo= "R2D2"
numero = "2026"
nombre = "UniversidadUTE"
identificador="DROIDE1"
print(codigo.isalnum())
print(codigo.isdigit())
print(codigo.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())
