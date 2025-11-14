from validaciones import num_mayor

def ord_nombre(listado_paises):  #ordenamiento por nombre
    temp = list(dic["nombre"] for dic in listado_paises) #se mete las nombres de los paises en una lista
    temp = sorted(temp) # se ordena usando sorted()
    
    print("--- ORDENAMIENTO POR NOMBRE (A-Z) ---")
    
    for pais in temp: #uso de iteracion para imprimir ordenadamente
        for i in listado_paises:
            if pais in i["nombre"]:
                print (f"-- {i["nombre"]} --")
                print ("")


def ord_superficie(listado_paises): #ordenamiento por por tamaño de la superficie
    temp = list(dic["superficie"] for dic in listado_paises) #se mete las superficies de los paises en una lista
    temp = sorted(temp) #se ordena usando sorted()
    
    print("--- ORDENAMIENTO SUPERFICIE ---")
    
    for pais in temp:  #uso de iteracion para imprimir ordenadamente
        for i in listado_paises:
            if pais == i["superficie"]:
                print (f"-- {i["nombre"]} tiene: {i["superficie"]}KM² --")
                print ("")


def ord_poblacion(listado_paises): #ordenamiento por cantidad de poblacion
    temp = list(dic["poblacion"] for dic in listado_paises) #la poblacion de los paises en una lista
    temp = sorted(temp) #se ordena usando sorted()
    
    print("--- ORDENAMIENTO POBLACIÓN ---")
    
    for pais in temp:  #uso de iteracion para imprimir ordenadamente
        for i in listado_paises:
            if pais == i["poblacion"]:
                print (f"-- {i["nombre"]} tiene: {i["poblacion"]} habitantes --")
                print ("")

def submenu_ord():
    print("""
            
            --- MENÚ ORDENAMIENTO ---
                (1) POR NOMBRE
                (2) POR SUPERFICIE
                (3) POR POBLACION

            
            """)
    while True:
        try:
            opcion = num_mayor()
            
            if opcion > 3:
                print("ERROR: Valor inválido, intente nuevamente.")
                continue
            break
        except ValueError:
            print("ERROR: Valor inválido, intente nuevamente.")
    return opcion

def submenu_match_orden():
    opcion = submenu_ord()
    match opcion:
        case 1:
            ord_nombre(listado_paises)
        case 2:
            ord_superficie(listado_paises)
        case 3:
            ord_poblacion(listado_paises)

listado_paises = [
    {"nombre":"argentina","poblacion":46994384,"superficie":2780400,"continente":"america"},
    {"nombre":"brasil","poblacion":220051512,"superficie":8515770,"continente":"america"},
    {"nombre":"francia","poblacion":68374591,"superficie":643801,"continente":"europa"},
    {"nombre":"japon","poblacion":123201945,"superficie":377915,"continente":"asia"},
    {"nombre":"maruecos","poblacion":37387585,"superficie":716550,"continente":"africa"},
    {"nombre":"canada","poblacion":38812500,"superficie":9976140,"continente":"america"},
    {"nombre":"australia","poblacion":25690614,"superficie":7692024,"continente":"oceania"},
    {"nombre":"italia","poblacion":60244639,"superficie":301340,"continente":"europa"},
    {"nombre":"india","poblacion":1393409038,"superficie":3287263,"continente":"asia"},
    {"nombre":"nigeria","poblacion":223804632,"superficie":923768,"continente":"africa"},
    {"nombre":"alemania","poblacion":83783942,"superficie":357022,"continente":"europa"},
    {"nombre":"mexico","poblacion":130262216,"superficie":1964375,"continente":"america"},
    {"nombre":"corea del sur","poblacion":51780579,"superficie":100210,"continente":"asia"},
    {"nombre":"sudafrica","poblacion":59308690,"superficie":1219090,"continente":"africa"},
    {"nombre":"nueva zelanda","poblacion":5082000,"superficie":268021,"continente":"oceania"},
    {"nombre":"chile","poblacion":19116201,"superficie":756102,"continente":"america"},
    {"nombre":"suiza","poblacion":8654622,"superficie":41285,"continente":"europa"},
    {"nombre":"rusia","poblacion":145912025,"superficie":17098242,"continente":"europa"},
    {"nombre":"turquia","poblacion":84339067,"superficie":783356,"continente":"europa"},
    {"nombre":"suecia","poblacion":10353442,"superficie":450295,"continente":"europa"},
    {"nombre":"finlandia","poblacion":5540720,"superficie":338424,"continente":"europa"}
]