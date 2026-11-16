print("CRUD DE UNIDADES DE TRANSPORTE EN PYTHON")
unidades_transporte = [
    {"id": 1, "nombre": "Juan Pérez", "unidad": "Trole-01", "estado": "En ruta"},
    {"id": 2, "nombre": "María Gómez", "unidad": "Ecovía-05", "estado": "En taller"},
    {"id": 3, "nombre": "Carlos Ruiz", "unidad": "Alimentador-12", "estado": "En ruta"}
]

def create():
    nuevo_id = len(unidades_transporte) + 1
    print("Registrar Nueva Unidad de Transporte")
    nombre = input("Nombre del operador: ")
    unidad = input("Unidad o Línea (ej. Trole-02): ")
    estado = input("Estado (En ruta, En taller, Fuera de servicio): ")
    nueva_unidad = {
        "id": nuevo_id,
        "nombre": nombre,
        "unidad": unidad,
        "estado": estado
    }
    unidades_transporte.append(nueva_unidad)
    print("Unidad registrada con éxito.")

def read():
    print("\n--- Lista de Unidades de Transporte ---")
    for item in unidades_transporte:
        print(f"ID: {item['id']} | Operador: {item['nombre']} | Unidad: {item['unidad']} | Estado: {item['estado']}")

def update():
    print("\n--- Actualizar Unidad de Transporte ---")
    id_update = int(input("Ingrese el ID a modificar: "))
    encontrado = False
    for item in unidades_transporte:
        if item["id"] == id_update:
            item["nombre"] = input("Nuevo nombre del operador: ")
            item["unidad"] = input("Nueva unidad o línea: ")
            item["estado"] = input("Nuevo estado (En ruta, En taller, Fuera de servicio): ")
            print("Unidad actualizada correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("ID no encontrado en el sistema.")

def delete():
    print("\n--- Eliminar Unidad de Transporte ---")
    id_delete = int(input("Ingrese el ID a borrar: "))
    encontrado = False
    for item in unidades_transporte:
        if item["id"] == id_delete:
            unidades_transporte.remove(item)
            print("Unidad eliminada del sistema.")
            encontrado = True
            break
    if not encontrado:
        print("ID no encontrado en el sistema.")

def menu():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE TRANSPORTE ===")
        print("1. Registrar unidad")
        print("2. Listar unidades")
        print("3. Modificar unidad")
        print("4. Eliminar unidad")
        print("5. Salir")
        opcion = input("Seleccione una opción (1 al 5): ")
        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Saliendo del sistema de transporte...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        
if __name__ == "__main__":
    menu()