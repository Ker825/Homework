def calcular_puntaje(fichas_rojas, fichas_azules, fichas_amarillas):
    """
    Calcula el puntaje total según las reglas:
    - Al cubo de las fichas rojas.
    - Más el doble de fichas azules.
    - Menos el cuadrado de las fichas amarillas.
    """
    return (fichas_rojas ** 3) + (2 * fichas_azules) - (fichas_amarillas ** 2)

def main():
    print("Bienvenido al juego de cálculo de puntaje.\n")
    fichas_rojas = 0
    fichas_azules = 0
    fichas_amarillas = 0

    while True:
        print("\nOpciones:")
        print("1. Andrés llegó en primer lugar (gana una ficha roja).")
        print("2. Andrés llegó en segundo lugar (gana una ficha azul).")
        print("3. Andrés llegó en tercer lugar (gana una ficha amarilla).")
        print("4. Calcular y mostrar puntaje.")
        print("5. Salir del programa.")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            fichas_rojas += 1
            print("Ganaste una ficha roja.")
        elif opcion == "2":
            fichas_azules += 1
            print("Ganaste una ficha azul.")
        elif opcion == "3":
            fichas_amarillas += 1
            print("Ganaste una ficha amarilla.")
        elif opcion == "4":
            puntaje = calcular_puntaje(fichas_rojas, fichas_azules, fichas_amarillas)
            print(f"\nFichas rojas: {fichas_rojas}, Fichas azules: {fichas_azules}, Fichas amarillas: {fichas_amarillas}")
            print(f"Tu puntaje total es: {puntaje}\n")
        elif opcion == "5":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
