print("CRUD DE LISTAS EN PYTHON")
advengers =[
    {"id":1, "nombre":"Tony Stark", "heroe":"Iron Man", "estado":"Activo"}
    {"id":2, "nombre":"Tony Stark", "heroe":"Iron Man", "estado":"Activo"}
    {"id":3, "nombre":"Tony Stark", "heroe":"Iron Man", "estado":"Activo"}
]

def create():
    id = 4
    print("Reclutar Advenger")
    nombre = input("Nombre del heroe")
    heroe = input("Heroe: ")
    estado = input("Estado (Activo, Retirado, Desaparecido)")
    nuevo_advenger = {
        "id":id,
        "nombre":nombre,
        "heroe":heroe,
        "estado":estado
    }
    advengers.append(nuevo_advenger)

def read():
    print("Lista de advengers")
    for advenger in advengers:
        print(f"{advenger["id"]} - nombre : {advenger["nombre"]}")

def update():
    print("Actualizar advenger")
    id_update = int(input("id a modificar"))
    for advenger in advengers:
        if (advenger[id]==id_update):
            advenger["nombre"] = input("Nuevo nombre")
            advenger["heroe"] = input("Nuevo heroe")
            advenger["estado"] = input("Nuevo estado")
            print("Actualizado")

def delete ():
    print("Eliminar advenger")
    id_delete = int(input("Id a borrar"))
    for advenger in advengers:
        if (advenger[id]==id_delete):
            advengers.remove(advenger)
            print("Advenger eliminado")


def menu():
    while True:
        print("Advenger")
        print("1. Crear")
        print("2. Leer")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Cerrar")
        opcion = input("Seleccione 1 al 5")
        if option=="1":
            create()
        elif option=="2":
            read()
        elif option=="3":
            update()
        elif option=="4":
            delete()
        elif option=="5":
            print("Saliendo del sistema")
            break
        else:
            print("Intente nueva opcion")
        
if __name__ = "__main__"