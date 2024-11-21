
import datetime
print("Este es un programa que calcula tu edad")
Nacimento= int(input("Por favor introduce año de nacimiento"))
Año_actual= datetime.datetime.now().year
Edad= Año_actual - Nacimento
print("Tu edad es:", Edad)
