 # primero creamos una lista llamada datos

import os
print("Se está ejecutando desde:", os.getcwd())

"""
datos = [
    ["BUENAS PRACTICAS DE DESARROLLO DE SOFTWARE", [2.85, 4.49, 5]],
    ["ESTADISTICA", [4.60, 5, 5]],
    ["ECUACIONES DIFERENCIALES", [3.47, 4.07, 4.60]],
    ["FISICA ONDAS Y OPTICA", [4.20, 4.07, 4.76]],
    ["ALGORITMO II", [5, 4.83, 4.54]],
    ["BIVE IV", [4.90]],
]

# VERSION ANTES DE LAS FUNCIONES
"""

"""
mejor = 0
peor = 5
mejor_materia = ""
peor_materia = ""


for elemento in datos:  # aqui uso el for para recorrer la lista para que me de la materia y su respectiva nota
    suma = 0
    notas = elemento[1]
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    print(elemento[0], elemento[1], ":", "el promedio es de:", (promedio))
    if promedio > mejor:
            mejor = promedio
            mejor_materia = elemento[0]
    if promedio < peor:
            peor = promedio
            peor_materia = elemento[0] 
print("La mejor materia fue:", mejor_materia, ";", "con un promedio de:", mejor)
print("La peor materia fue:", peor_materia, ";", "con un promedio de:", peor)



for i in range(len(datos)):
      print(i, " - ", datos[i][0])

opcion = int(input("Elige el numero de la materia: "))
nueva_nota = float(input("Ingrese la nueva nota: "))
datos[opcion][1].append(nueva_nota)
print("Notas actualizadas: ", datos[opcion][1])

suma_total = 0
cantidad_total = 0

for elemento in datos:
      notas = elemento[1]
      for nota in notas:
            suma_total += nota
            cantidad_total += 1
            promedio_general = suma_total / cantidad_total
print("Tu promedio general es de:", promedio_general)


mejor_nota = 0
mejor_materia = ""
for elemento in datos:
    notas = elemento[1]
    for nota in notas:
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_materia = elemento [0]
print("La mejor nota del semestre es:", mejor_nota,"y esta en",mejor_materia)
"""


def menu():
     print("\n === Web de Notas === ")
     print("1. Ver reporte completo de notas")
     print("2. Agregar nota")
     print("3. Ver promedio general")
     print("4. Salir del menu ")

def ver_reporte(datos):
    mejor = 0
    peor = 5
    mejor_materia = ""
    peor_materia = ""

    for elemento in datos:
        suma = 0 
        notas = elemento[1]
        
        for nota in notas:
            suma += nota
        promedio = suma / len(notas)
        print(elemento[0], elemento[1], ":", "Promedio es de:", (promedio))

        if promedio > mejor:
                mejor = promedio
                mejor_materia = elemento[0]

        if promedio < peor:
                peor = promedio
                peor_materia = elemento[0] 

    print("La mejor materia fue:", mejor_materia, ";", "con un promedio de:", mejor)
    print("La peor materia fue:", peor_materia, ";", "con un promedio de:", peor)


def agregar_nota(datos):
          materia = input("Ingrese el nombre de la materia: ").upper()
          encontrada = False
                    
          while True:  # para pedir la nota y validarla
                         try:
                              nueva_nota = float(input("Ingrese la nueva nota:"))
                         except:
                              print("Debe ingresar un numero valido ")
                              continue
                         if nueva_nota < 0 or nueva_nota > 5:
                              print("La nota debe ser entre 0 y 5.")
                              continue
                         break
          
          for elemento in datos:
               if elemento[0].upper == materia:
                    elemento[1].append(nueva_nota)
                    print("Nota agregada correctamente")
                    guardar_datos(datos)
                    encontrada == True
                    break
                     
          if not encontrada:
               datos.append([materia, [nueva_nota]])
               print("Materia creada y nota agregada")
               guardar_datos(datos)

def promedio_total(datos):
          suma_total = 0
          cantidad_total = 0
          for elemento in datos:
               notas = elemento[1]
               for nota in notas:
                    suma_total += nota
                    cantidad_total += 1
                    promedio_general = suma_total / cantidad_total
          print("Tu promedio general es de:", promedio_general)

def guardar_datos(datos):
     archivo = open("datos.txt", "w" )
     print("Archivo creado o actualizado")


     for elemento in datos:
          nombre = elemento[0]
          notas = elemento[1]

          linea = nombre

          for nota in notas:
               linea = linea + "," + str(nota)

          archivo.write(linea + "\n")

     archivo.close()

def cargar_datos():
     datos = []               # creo una lista vacia
     try:     # el try es para intentar abrir el archivo por si no existe la primera vez y asi evitamos que se rompa el programa

          with open("datos.txt", "r" ) as archivo: # abre el archivo con el nombre datos.txt en modo lectura por eso se pone r y el with hace que se cierre automaticamente
               for linea in archivo:
                    linea = linea.strip()  # elimina saltos de linea y espacios al inicio o final
                    partes = linea.split(",")  # divide la linea usando coma como separador y devuelve una lista strings

                    nombre = partes[0] # el nombre de cada materia
                    notas = []

                    for nota in partes[1:]:  # para recorrer solo la posicion de las notas
                         notas.append(float(nota))  # convierte la nota de string a numero decimal
                    datos.append([nombre, notas])

     except:
          print("No se encontró el archivo. se creará uno nuevo")
     
     return datos
 
if __name__ == "__main__":
    datos = cargar_datos()
    while True:
     menu()
     try :
         opcion = int(input("Ingrese una opcion "))
     except: 
         print("Debe ingresar un numero.")
         continue
     if opcion < 1 or opcion > 4:
          print("Opcion invalida")
          continue
     if opcion == 1:
           ver_reporte(datos)
     elif opcion == 2:
           agregar_nota(datos)
     elif opcion == 3:
           promedio_total(datos)
     elif opcion == 4:
          print("\n === HASTA LUEGO === ")
          break


