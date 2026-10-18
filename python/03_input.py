print("Incluir Datos con Input")
nombre=input("¿Cual es su nombre?: ")
print("Hola", nombre)
print("Bienvenido a SpringField")
print("Hasta luego " +nombre)

cantidad = int(input("¿Cuantas rosquillas hay?: "))
total = cantidad + 2
print("Rosquillas totales: ", total)


print("Conversiones")
print("=== Tienda de APU ===")
nombre_cliente = input("NOmbre cliente: ")
precio = float(input("Precio de Rosquillas: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad
print("Total a pgar: ", total)
print("Total a pagar(round): ", round(total, 2))
print(f"Total a pagar(f): ${total:.2f}")
