print("Condicional if")
print("Condicional Simple")
dinero=10
if dinero==5:
    print("Homero puede comprar rosquillas")

print("Programa finalizó")


print("Condicional if - else")
print("Condicional dos caminos")
creditos = float(input("Cantidad de creditos disponibles"))
precio_repuesto = float(input("Precio repuesto"))

if(creditos>=precio_repuesto):
    print("Cmpra autorizada")
else:
    print("Créditos insuficientes")
    print("Buscar solucion o trueque")




print("Condicional if- elif- else")
print("Condicional condiciones anidadas")
combustible = float(input("Combustible de la nave"))
motor_funciona = input("El motor funciona SI O NO")

if (combustible>=75):
    print("Òptimo")
elif(combustible>=50):
    print("Suficiente")
elif(combustible>=20):
    print("Bajo")
else:
    print("Crítico")
    print("Localiza Base mas cercana")




piloto = input("Nombre del piloto")
print("Motor verificado")
combustible = int(input("Combustible disponible")) 

if (motor_funciona == "SI"):
    print("Motor Verificado")
    if (combustible>=50):
        print("Combustible disponible")
        print("Participacion disponible")
    else:
        print("LDebe recargar combustible")
else: 
    print("No puede participar")
    print("El motor necesita reparacion")