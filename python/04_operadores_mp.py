print("OPERADORES")
print("Operadores Aritméticos")
print("+ Suma: ",5, "+", 3, "=", 5+3)
print("- Resta: ",5, "-", 3, "=", 5-3)
print("* Multiplicación: ",5, "*", 3, "=", 5*3)
print("/ División: ",5, "/", 3, "=", 5/3)
print("// División Entera: ",5, "//", 3, "=", 5//3)
print("% Módulo: ",5, "%", 3, "=", 5%3)
print("** Potencia: ",5, "**", 3, "=", 5**3)
print("% Residuo: ",10, "%", 3, "=", 10%3)


print("Tabla de multiplicar del 5 (Cálculo de tarifas)")
print(5, "*", 1, "=", 5*1)
print(5, "*", 2, "=", 5*2)
print(5, "*", 3, "=", 5*3)
print(5, "*", 4, "=", 5*4)
print(5, "*", 5, "=", 5*5)
print(5, "*", 6, "=", 5*6)
print(5, "*", 7, "=", 5*7)
print(5, "*", 8, "=", 5*8)
print(5, "*", 9, "=", 5*9)
print(5, "*", 10, "=", 5*10)


print("OPERADORES DE COMPARACION")
print("== Igual a: ", 5, "==", 5, 5==5)
print("== Igual a: ", 5, "==", 4, 5==4)
print("!= Igual a: ", 5, "==", 4, 5!=4)
print("!= Igual a: ", 5, "==", 5, 5!=5)
print("> Mayor que: ", 10, ">", 8, 10>8)
print("> Mayor que: ", 10, ">", 8, 10>8)
print("< Menor que: ", 10, "<", 18, 10<18)
print("< Menor que: ", 10, "<", 18, 10<18)

print(">= Mayor o igual que: ", 10, ">=", 8, 10>=8)
print(">= Mayor o igual que: ", 10, ">=", 18, 10>=18)
print("<= Menor o igual que: ", 10, "<=", 18, 10<=18)
print("<= Menor o igual que: ", 10, "<=", 18, 10<=18)

print("OPERADORES LOGICAS")
print("Operadores and : (5==5)and(4>3)=", (5==5)and(4>3))
print("Operadores and : (5==5)and(4>8)=", (5==5)and(4>8))
print("Operadores or : (5==5)and(4>3)=", (5==5)or(4>8))
print("Operadores or : (5==6)and(4>8)=", (5==6)or(4>8))
print("Operadores not : not (5==6)", not (5==6))
print("Operadores not : not (5==5)", not (5==5))

tiene_saldo = True
terminal_abierta = True

puede_viajar = tiene_saldo and terminal_abierta
print("Puede realizar el viaje: ", puede_viajar)