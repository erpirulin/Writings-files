names = ["John", "Oscar", "Jacob"]
 
file = open("names.txt", "w+")
#escribir los nombres en el archivo
for name in names:
    files = name
    print(files)
file.close()
 
file= open("names.txt", "r")
#salida del contenido del archivo en la consola
file.close()
