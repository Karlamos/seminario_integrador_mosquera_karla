print("Incluir Datos con Input")
nombre = input("¿Cuál es su nombre?: ")
print("Hola", nombre)
print("Bienvenido a Terminal Carcelén")
print("Hasta luego " + nombre)

cantidad = int(input("¿Cuántos pasajeros suben?: "))
total = cantidad + 2
print("Pasajeros totales: ", total)


print("Conversiones")
print("=== Taquilla del Trole ===")
nombre_cliente = input("Nombre cliente: ")
precio = float(input("Precio del pasaje: "))
cantidad = int(input("Cantidad de pasajes: "))
total = precio * cantidad
print("Total a pagar: ", total)
print("Total a pagar (round): ", round(total, 2))
print(f"Total a pagar (f): ${total:.2f}")