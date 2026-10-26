for flexion in range(1,6):
    print("Goku hace la flexion", flexion)

for numero in range(1,11):
    print("Multiplicaion", 5, "*", numero, "=", 5*numero)

for numero in range(1,11,3):
    print("Multiplicaion", 5, "*", numero, "=", 5*numero)


avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 2, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"},
    {"id": 3, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": "Activo"}
]

print("----------------Lista avengers----------------")
for avenger in avengers:
    print(f"{avenger['id']} nombre: {avenger['nombre']}")


nombres = ["Pedro", "Pablo", "Juan"]
for nombre in nombres:
    print("Nombre actual:", nombre)



guerreros ={
    "Goku": 9500,
    "Vegeta": 6000,
    "Gohan": 6000,
    "Piccolo": 4500
}

for nombre, poder in guerreros.items():
    if poder >= 9000:
        print(nombre, "Puede enfrentar a Freezer")
    else:
        print(nombre, "necesita entrenar")


print("Ciclo for anidados")
guerreros =["Goku","Vegeta","Gohan","Piccolo", "Trunks", "Majinbu"]
for guerrero in guerreros:
    print("Turno de:", guerrero)
    for ronda in range(1,4):
        print("Ronda: ", ronda)



print("---------------Break y Continue--------------")
for guerrero in guerreros:
    print("Guerrero", guerrero)
    if(guerrero == "Piccolo"):
        break
    if(guerrero == "Vegeta"):
        continue
    print("Guerrero ",guerrero)