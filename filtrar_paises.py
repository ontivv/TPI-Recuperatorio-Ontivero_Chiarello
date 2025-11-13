

def f_continente(continente,listado_paises):# filtra paises por continente         #le pasamos el continente y la lista de paises
    print (f"<-----paises en {continente}----->")
    for pais in listado_paises:
        if continente == pais["continente"]: #si el continente del pais iterado coincide con el del usurio se imprime
            print (f"+ {pais["nombre"]}")


    return "<--------------------------------->"

def f_poblacion(p_menor,p_mayor,listado_paises): # filtra paises por cantidad de poblacion #le pasamos como parametros los dos valores de filtrdo que eligio el usuario
    print ("-----paises con poblacion de...---")                       #y la lista de paises
    print (f"-----{p_menor} hasta {p_mayor}-----")
    for pais in listado_paises:
        if p_menor <= pais["poblacion"] and p_mayor >=  pais["poblacion"]: #verifica si el pais esta en el rango de poblacion elegido por el usuario
            print(f"+ {pais["nombre"]} :{pais["poblacion"]} de habitantes")
    print ("<--------------------------------->")
    return ""

def f_superficie(superficie_menor,superficie_mayor,listado_paises):  #filtra paises por tamaño de superficie #le pasamos como parametros los dos valores del rango de superficie elegidos por el usuario
    print ("-----paises con superficie entre-----")                    #y la lista de paises
    print (f"-----{superficie_menor} hasta {superficie_mayor}-----")
    for pais in listado_paises:
        if superficie_menor <= pais["superficie"] and superficie_mayor >=  pais["superficie"]: #verifica si el pais esta en el rango de superficie elegido por el usuario
            print(f"+ {pais["nombre"]} :{pais["superficie"]}km²")
    print ("<--------------------------------->")
    return ""

