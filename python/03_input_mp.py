# Incluir Datos con Input
print("Incluir Datos con Input")
nombre = input("¿Cuál es su nombre?: ")
print("Hola", nombre)
print("Bienvenido a la Terminal de Transporte")
print("Hasta luego " + nombre)

cantidad = int(input("¿Cuántas unidades hay?: "))
total = cantidad + 2
print("Unidades totales: ", total)


print("Conversiones")
print("=== Taquilla de la Estación ===")
nombre_cliente = input("Nombre cliente: ")
precio = float(input("Precio del pasaje: "))
cantidad = int(input("Cantidad de pasajes: "))
total = precio * cantidad
print("Total a pagar: ", total)
print("Total a pagar(round): ", round(total, 2))
print(f"Total a pagar(f): ${total:.2f}")