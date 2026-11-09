for recorrido in range(1, 6):
    print("La unidad completa el recorrido", recorrido)

for numero in range(1, 11):
    print("Frecuencia", 5, "*", numero, "=", 5 * numero)

for numero in range(1, 11, 3):
    print("Frecuencia", 5, "*", numero, "=", 5 * numero)


unidades_transporte = [
    {"id": 1, "nombre": "Juan Pérez", "unidad": "Trole-01", "estado": "En ruta"},
    {"id": 2, "nombre": "María Gómez", "unidad": "Ecovía-05", "estado": "En ruta"},
    {"id": 3, "nombre": "Carlos Ruiz", "unidad": "Alimentador-12", "estado": "En ruta"}
]

print("---------------- Lista de Unidades ----------------")
for item in unidades_transporte:
    print(f"{item['id']} unidad: {item['unidad']}")


conductores = ["Pedro", "Pablo", "Juan"]
for conductor in conductores:
    print("Conductor en turno:", conductor)



operadores_flota = {
    "Juan": 9500,
    "María": 6000,
    "Carlos": 6000,
    "Ana": 4500
}

for nombre, kilometros in operadores_flota.items():
    if kilometros >= 9000:
        print(nombre, "califica para bono de eficiencia")
    else:
        print(nombre, "necesita completar kilometraje")


print("Ciclos for anidados")
unidades = ["Trole-01", "Ecovía-02", "Alimentador-03", "Alimentador-04", "Trole-05", "Ecovía-06"]
for unidad in unidades:
    print("Revisión de unidad:", unidad)
    for turno in range(1, 4):
        print("Turno operativo: ", turno)


print("--------------- Break y Continue --------------")
for unidad in unidades:
    print("Unidad actual", unidad)
    if unidad == "Alimentador-03":
        break
    if unidad == "Ecovía-02":
        continue
    print("Unidad verificada ", unidad)