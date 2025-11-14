def buscar_pais(nombre_pais,listado_paises):
    for pais in listado_paises:
        if nombre_pais == pais["nombre"]:
            print ("")
            return pais
    return "ERROR no registrado"
            