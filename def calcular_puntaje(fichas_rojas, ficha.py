def calcular_puntaje(fichas_rojas, fichas_azules, fichas_amarillas):
    """
    Las reglas que se usan para calcular el puntaje son:
    - El ganador recibe una ficha roja, que es el cubo de estas.
    - El segundo lugar recibe la azul, que es más el doble de fichas azules.
    - El último recibe una amarrila, que es menos el cuadrado de las fichas amarillas.
    """
    return (fichas_rojas ** 3) + (2 * fichas_azules) - (fichas_amarillas ** 2)

def main():
    print("Este es un pograma que permite saber el puntaje de un jugador en base a la cantidad de fichas ganadas.\n")

    # Preguntar si el usuario desea continuar
    continuar = input("¿Quieres continuar? (si/no): ").strip().lower()
    if continuar != "sí" and continuar != "si":
        print("Gracias por visitar el programa. ¡Adiós!")
        return

    fichas_rojas = 0
    fichas_azules = 0
    fichas_amarillas = 0

    while True:
    # Aquí se le darán varias opciones para escoger al jugador 
    # Dependiendo de que escoja, se le dará la opción de introducir valores o realizar el calculo y si quiere finalizar al programa
        print("\nOpciones:")
        print("1. Insertar fichas ganadas en esta ronda.")
        print("2. Calcular y mostrar puntaje acumulado.")
        print("3. Salir del programa.")

        try:
            opcion = int(input("Elige una opción (1-3): "))

            if opcion == 1:
            # Aquí se escogió la opción uno, por lo tanto se le pedirá que intoduzca las cantidades de las fichas ganadas
                try:
                    rojas = int(input("Ingresa el número de fichas rojas ganadas: "))
                    azules = int(input("Ingresa el número de fichas azules ganadas: "))
                    amarillas = int(input("Ingresa el número de fichas amarillas ganadas: "))
                    
                    fichas_rojas += rojas
                    fichas_azules += azules
                    fichas_amarillas += amarillas

                    print(f"Fichas actualizadas: {fichas_rojas} rojas, {fichas_azules} azules, {fichas_amarillas} amarillas.")
                except ValueError:
                    #Si pone otro caracter que no sea númerico, imprimirá lo siguiente:
                    print("Por favor, ingresa valores numéricos válidos.")
            elif opcion == 2:
            # Se escogió la opción dos, por lo tanto se calculará la el valor de la cantidad de fichas que se ganaron
                puntaje = calcular_puntaje(fichas_rojas, fichas_azules, fichas_amarillas)
                print(f"\nFichas totales: {fichas_rojas} rojas, {fichas_azules} azules, {fichas_amarillas} amarillas.")
                print(f"El puntaje total es: {puntaje}\n")
            elif opcion == 3:
            #Se escogío la opción 3, por lo tanto se imprime el mensaje dado y se "Rompe" el programa
                print("Juego finalizado, hasta pronto.")
                break
            else:
            #Cualquie valor que no sea 1-3, se detecta como erro y imprime:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
        # Manejar entradas no válidas
            print("Entrada inválida. Por favor, ingresa un número entre 1 y 3.")

# Se asegura que cierta parte del código se ejecutará solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
