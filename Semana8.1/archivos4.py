# Solicitar nombres, apellidos, edad y carrera de un estudiante y guardar en un archivo.
nombres = input("Dime tu nombre: ")
apellidos = input("Dime tus apellidos: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu carrera: ")
datos = f"Nombres: {nombres}, \nApellidos: {apellidos}, \nEdad: {edad}, \nCarrera: {carrera}".title()

with open("estudiante.txt", "w", encoding = "utf-8") as archivo:
    archivo.write(datos)

print("Guardado.")