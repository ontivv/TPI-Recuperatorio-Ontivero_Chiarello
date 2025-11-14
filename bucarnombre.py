def buscar_pais(nombre_pais,listado_paises):  #funcion para buscar nombre
    for pais in listado_paises: #itera la lista hasta que coincida con nombre mandado como parametro
        if nombre_pais == pais["nombre"]:
            print ("")
            return pais  #si el pais es encontrado retorna
    return "ERROR no registrado" #si no es encontrado dara este mensaje
            