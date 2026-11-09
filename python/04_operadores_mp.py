print("OPERADORES EN GESTIÓN DE TRANSPORTE")
print("Operadores Aritméticos de Flota")
print("+ Suma de pasajeros: ", 5, "+", 3, "=", 5 + 3)
print("- Resta de pasajeros: ", 5, "-", 3, "=", 5 - 3)
print("* Multiplicación de aforo: ", 5, "*", 3, "=", 5 * 3)
print("/ División de ruta: ", 5, "/", 3, "=", 5 / 3)
print("// División Entera de unidades: ", 5, "//", 3, "=", 5 // 3)
print("% Módulo de validaciones: ", 5, "%", 3, "=", 5 % 3)
print("** Potencia de capacidad: ", 5, "**", 3, "=", 5 ** 3)
print("% Residuo de pasajeros: ", 10, "%", 3, "=", 10 % 3)


print("Tabla de frecuencia de unidades (Factor 5)")
print(5, "*", 1, "=", 5 * 1)
print(5, "*", 2, "=", 5 * 2)
print(5, "*", 3, "=", 5 * 3)
print(5, "*", 4, "=", 5 * 4)
print(5, "*", 5, "=", 5 * 5)
print(5, "*", 6, "=", 5 * 6)
print(5, "*", 7, "=", 5 * 7)
print(5, "*", 8, "=", 5 * 8)
print(5, "*", 9, "=", 5 * 9)
print(5, "*", 10, "=", 5 * 10)


print("OPERADORES DE COMPARACIÓN")
print("== Igual a: ", 5, "==", 5, 5 == 5)
print("== Igual a: ", 5, "==", 4, 5 == 4)
print("!= Diferente de: ", 5, "!=", 4, 5 != 4)
print("!= Diferente de: ", 5, "!=", 5, 5 != 5)
print("> Mayor que: ", 10, ">", 8, 10 > 8)
print("> Mayor que: ", 10, ">", 8, 10 > 8)
print("< Menor que: ", 10, "<", 18, 10 < 18)
print("< Menor que: ", 10, "<", 18, 10 < 18)

print(">= Mayor o igual que: ", 10, ">=", 8, 10 >= 8)
print(">= Mayor o igual que: ", 10, ">=", 18, 10 >= 18)
print("<= Menor o igual que: ", 10, "<=", 18, 10 <= 18)
print("<= Menor o igual que: ", 10, "<=", 18, 10 <= 18)

print("OPERADORES LÓGICOS")
print("Operadores and : (5==5) and (4>3) =", (5 == 5) and (4 > 3))
print("Operadores and : (5==5) and (4>8) =", (5 == 5) and (4 > 8))
print("Operadores or : (5==5) or (4>8) =", (5 == 5) or (4 > 8))
print("Operadores or : (5==6) or (4>8) =", (5 == 6) or (4 > 8))
print("Operadores not : not (5==6) =", not (5 == 6))
print("Operadores not : not (5==5) =", not (5 == 5))

tiene_saldo = True
validador_activo = True

puede_ingresar = tiene_saldo and validador_activo
print("¿Puede ingresar al sistema?:", puede_ingresar)