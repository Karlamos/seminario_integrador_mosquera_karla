print("Condicional if")
print("Condicional Simple")
saldo_tarjeta = 10
if saldo_tarjeta == 5:
    print("El usuario puede validar su pasaje")

print("Programa finalizó")


print("Condicional if - else")
print("Condicional dos caminos")
saldo_disponible = float(input("Cantidad de saldo disponible: "))
precio_pasaje = float(input("Precio del pasaje: "))

if saldo_disponible >= precio_pasaje:
    print("Compra autorizada")
else:
    print("Saldo insuficiente")
    print("Recargue en taquilla o estación")




print("Condicional if- elif- else")
print("Condicional condiciones anidadas")
aforo_actual = float(input("Porcentaje de aforo de la unidad: "))
operativa = input("¿La unidad está en ruta? SI O NO: ")

if aforo_actual >= 75:
    print("Óptimo")
elif aforo_actual >= 50:
    print("Suficiente")
elif aforo_actual >= 20:
    print("Bajo")
else:
    print("Crítico")
    print("Enviar unidad de refuerzo a la estación")




nombre_operador = input("Nombre del operador: ")
print("Unidad verificada")
aforo_unidades = int(input("Pasajeros actuales a bordo: "))

if operativa == "SI":
    print("Unidad en Ruta Verificada")
    if aforo_unidades >= 50:
        print("Aforo disponible en parámetro normal")
        print("Operación habilitada")
    else:
        print("Debe esperar más pasajeros en terminal")
else:
    print("No puede operar en ruta")
    print("La unidad necesita mantenimiento en taller")