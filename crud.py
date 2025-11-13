import csv
import os

def creacion_csv(): #crea un csv si no existe
    if not os.path.exists("paises.csv"):   # verifica si paises csv ya esta creado si no es así sigue
        with open ("paises.csv","a",encoding="UTF-8",newline="")as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader() 

def añadir_csv(dic):  #añade un diccionario a la lista
    if os.path.exists("paises.csv"): # verifica si paises csv ya esta creado si es así sigue
        with open("paises.csv","a")as archivo: #abrimos en modo lectura pero sin perder datos
            escritor = csv.DictWriter(archivo,fieldnames=["nombre","poblacion","superfie","continente"])
            escritor.writerow({"nombre":dic["nombre"],"poblacion":dic["poblacion"],"superficie":dic["superficie"],"continente":dic["continente"]})   #añade el diccionario que pasamos como parametro
            
def actualizar_csv(lista_libros):  #hace cambios en el csv
    lista = []
    if os.path.exists("paises.csv"): # verifica si paises csv ya esta creado si es así sigue
        with open("paises.csv","w")as archivo: #abrimos en modo escritura
            escritor = csv.DictWriter(archivo,fieldnames=["nombre","poblacion","superfie","continente"]) 
            escritor.writeheader()
            for i in lista_libros: #bucle que reescribe el diccionario
                    escritor.writerow({"nombre":i["nombre"],"poblacion":i["poblacion"],"superficie":i["superficie"],"continente":i["continente"]})
        
def cargar_datos(): #carga una lista con diccionarios a una variable
    if os.path.exists("paises.csv"): #verifica si paises csv ya esta creado si es así sigue
        lista = []
        with open("paises.csv","r")as archivo: #abrimos en modo lectura
            escritor = csv.DictReader(archivo,fieldnames=["nombre","poblacion","superficie","continente"])
            for i in escritor: #bucle que añade los diccionarios del csv a la lista 
                lista.append({"nombre":i["nombre"],"poblacion":i["poblacion"],"superficie":i["superficie"],"continente":i["continente"]})
        return lista
    else:
        print("ERROR: paises.csv no existe.")
        return[]

