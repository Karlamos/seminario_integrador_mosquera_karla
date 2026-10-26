poder = 2000
while poder < 10000:
    print("Vegeta está entrenando")
    poder+=2000
print("Vegeta alcanzó su objetivo")


while poder>0:
    print("Majinbu tiene ",poder ,"de poder")
    poder -=500
print("Majinbu quedó sin energia")

print("--------------------Continue y break----------------------")
dia=0
while dia<0:
    dia+=1
    if dia == 4:
        print("Dia 4: gohan estudia")
        continue
    print("Dia", dia, "Gohan entrena")
    if dia == 8:
        print("Fin del sistema")
        break


print("-----------------------Ejercicio-------------------------")
for sector in range(1, 11):
    if sector == 3:
        print(f"Sector {sector}: Trunks detecta una zona destruida y decide omitirla.")
        continue
    elif sector == 7:
        print(f"Sector {sector}: ¡Se encontró a los androides 17 y 18! Se detiene la búsqueda.")
        break
    
    print(f"Sector {sector}: Trunks realiza la exploración normalmente.")