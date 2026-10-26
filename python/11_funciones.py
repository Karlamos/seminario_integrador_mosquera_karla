print("---------Funciones---------")
print("Autor: Karla Mosquera")

def kamehameha():
    print("Karla concentra su energia")
    print("!Kamehameha")

kamehameha()
kamehameha()
kamehameha()
kamehameha()



def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegeta")
atacar("Karla")



def calcular_poder(poder, ataques):
    danio= poder * ataques
    return danio

resultado = calcular_poder(4,26)
print("El poder de Karla Mosquera es:",resultado)

resultado = calcular_poder(4,5000)
print("El poder de Goku es:",resultado)


def transformar_sayajin(nombre, poder):
    if poder>=9000:
        print(f"Transformacion de {nombre} a SuperSayajing exitosa")
    else:
        print(f"{nombre} Necesita aumentar su poder ")

transformar_sayajin("Karla Mosquera", 5000)
transformar_sayajin("Gohan", 15000)


nombre_persobnaje: str = "Goku"
edad: int= 33
es_activo: bool = True

def multiplicador_poder(entrenamiento:float, edad:int)->float:
    return entrenamiento*edad

poder:float = multiplicador_poder(15.5,2)
print("poder calculado ", poder)