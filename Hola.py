# Solicitar al usuario que ingrese dos números
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Suma
suma = a + b
print("La suma de", a, "y", b, "es:", suma)

# Resta
resta = a - b
print("La resta de", a, "y", b, "es:", resta)

# Multiplicación
multiplicacion = a * b
print("La multiplicación de", a, "y", b, "es:", multiplicacion)

# División
if b != 0:
    division = a / b
    print("La división de", a, "y", b, "es:", division)
else:
    print("Error: No se puede dividir por cero.")
