def ord_nombre(listado_paises):  #ordenamiento por nombre
    temp = list(dic["nombre"] for dic in listado_paises) #se mete las nombres de los paises en una lista
    temp = sorted(temp) # se ordena usando sorted()
    for pais in temp: #uso de iteracion para imprimir ordenadamente
        for i in listado_paises:
            if pais in i["nombre"]:
                print (i["nombre"])
                print ("")


def ord_superficie(listado_paises): #ordenamiento por por tamaño de la superficie
    temp = list(dic["superficie"] for dic in listado_paises) #se mete las superficies de los paises en una lista
    temp = sorted(temp) #se ordena usando sorted()
    for pais in temp:  #uso de iteracion para imprimir ordenadamente
        for i in listado_paises:
            if pais == i["superficie"]:
                print (f"{i["nombre"]} tiene: {i["superficie"]}KM²")
                print ("")


def ord_poblacion(listado_paises): #ordenamiento por cantidad de poblacion
    temp = list(dic["poblacion"] for dic in listado_paises) #la poblacion de los paises en una lista
    temp = sorted(temp) #se ordena usando sorted()
    for pais in temp:  #uso de iteracion para imprimir ordenadamente
        for i in listado_paises:
            if pais == i["poblacion"]:
                print (f"{i["nombre"]} tiene: {i["poblacion"]} habitantes")
                print ("")
