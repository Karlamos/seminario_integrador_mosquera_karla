kilometraje = 2000
while kilometraje < 10000:
    print("La unidad está completando recorrido")
    kilometraje += 2000
print("La unidad alcanzó su meta de kilometraje")


while kilometraje > 0:
    print("La unidad tiene ", kilometraje, " de combustible restante")
    kilometraje -= 500
print("La unidad quedó sin combustible")

print("--------------------Continue y break----------------------")
dia = 0
while dia < 0:
    dia += 1
    if dia == 4:
        print("Día 4: operador realiza mantenimiento")
        continue
    print("Día", dia, " operador conduce en ruta")
    if dia == 8:
        print("Fin del sistema")
        break


print("-----------------------Ejercicio-------------------------")
for sector in range(1, 11):
    if sector == 3:
        print(f"Sector {sector}: La unidad detecta un bache en la vía y decide omitirla.")
        continue
    elif sector == 7:
        print(f"Sector {sector}: ¡Se encontró control de pasajeros en la parada 17! Se detiene la revisión.")
        break
    
    print(f"Sector {sector}: La unidad realiza el recorrido normalmente.")