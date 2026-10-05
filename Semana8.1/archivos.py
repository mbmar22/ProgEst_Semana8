# Leer un archivo llamado datos.txt
archivo = open("datos.txt", "r") # La r sirve para decir que solo es lectura.
print(archivo.read())
archivo.close