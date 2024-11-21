print("Este programa determina el mayor número de tres que introduzcas")
    continuar = input("¿Quieres continuar? (si/no): ").strip().lower()
    if continuar == "sí" or continuar == "si":
    # Aquí, ya el usario accedió a continuar, así que proceguirá a pedirle 3 números
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            num3 = float(input("Introduce el tercer número: "))
            break  # Si todo va bien, salimos del bucle
        except ValueError:
            print("No escribiste un valor númerico. Por favor ingresa un número.")

    # Aquí se compara todo los números ingresador previamente
    mayor = max(num1, num2, num3,)

    # Aqui el Print va a mostrar el número mayor de todos los que hemos introducido
    print(f"El mayor de los números es: {mayor}")
    #Aquí el usuario ya obtuvo el mayor número, así que el Elif va a hacer que se cierr el programa
elif continuar == "no":
    print("Okay, nos vemos en otra ocasión.")
    #Aquí el usario respondió no así que el programa se dejará de ejecutar
else:
    print("Por favor, responde solo si o no")