print("---------Funciones en Transporte Público---------")
print("Autor: Karla Mosquera")

def activar_sistema():
    print("El operador concentra el sistema")
    print("!Unidad en Ruta")

activar_sistema()
activar_sistema()
activar_sistema()
activar_sistema()



def operar_unidad(unidad):
    print(unidad, "inicia recorrido operativo")

operar_unidad("Trole-01")
operar_unidad("Ecovía-02")
operar_unidad("Karla")



def calcular_eficiencia(kilometros, viajes):
    rendimiento = kilometros * viajes
    return rendimiento

resultado = calcular_eficiencia(4, 26)
print("El rendimiento de Karla Mosquera es:", resultado)

resultado = calcular_eficiencia(4, 5000)
print("El rendimiento de la Unidad 01 es:", resultado)


def verificar_unidad(nombre, pasajeros):
    if pasajeros >= 50:
        print(f"La unidad {nombre} opera con aforo completo exitoso")
    else:
        print(f"La unidad {nombre} necesita incorporar más pasajeros")

verificar_unidad("Karla Mosquera", 5000)
verificar_unidad("Unidad-05", 15000)


nombre_operador: str = "Juan"
edad: int = 33
es_activo: bool = True

def multiplicador_kilometraje(kilometros: float, turnos: int) -> float:
    return kilometros * turnos

kilometraje_total: float = multiplicador_kilometraje(15.5, 2)
print("Kilometraje calculado: ", kilometraje_total)