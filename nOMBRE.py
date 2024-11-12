print("Hola, le voy a hacer una serie de preguntas como parte de un censo.")
print("Espero que no le moleste que le quite unos minutos de su tiempo.")

def main():
    while True:
        continuar = input("¿Deseas que se te haga la encuesta? (Sí/No): ").strip().lower()
        
        if continuar == "no":
            print("Okay, cuando tenga tiempo, llámenos.")
            return  # Detiene la ejecución de la función y, por lo tanto, del programa
        elif continuar == 'sí':
            print("Continuando la encuesta...")
            break  # Salimos del bucle para continuar con la encuesta
        else:
            print("Respuesta no válida. Por favor, escribe 'sí' o 'no'.")

    name = input("Por favor, introduce tu nombre: ")
    print("Mucho gusto en conocerte,", name, "¿podrías decirme tu edad?")
    
    while True:
        try:
            edad = int(input("Edad: "))
            break
        except ValueError:
            print("Por favor, dame un número, no otra cosa :D")

    direccion = input("Ahora, dame tu dirección donde resides, por favor: ")
    print("Gracias por tu participación. Tu información es valiosa.")

if __name__ == "__main__":
    main()