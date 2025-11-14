from validaciones import num_mayor

def pais_mayor_menor_poblacion(listado_paises,opcion):  #funcion para pais 
    mayor = 0
    menor = 9999999999999999990
    
    for pais in listado_paises:
        if pais["poblacion"] >= mayor:
            mayor = pais["poblacion"]
            pais_mayor = pais["nombre"]
        if pais["poblacion"] < menor:
            menor = pais["poblacion"]
            pais_menor = pais["nombre"]
    
    if opcion == 1:
        print (f"El país con menor población es: {pais_menor}")
    elif opcion == 2:
        print (f"El país con mayor población es: {pais_mayor}")
    else:
        print("ERROR: Valor inválido.")

def promedio(listado_paises,opcion):
    suma = 0
    cant = 0
    prom = 0
    palabra = ""
    
    if opcion == 3:
        palabra = "poblacion"
    elif opcion == 4:
        palabra = "superficie"
        
    for pais in listado_paises:
        suma += pais[palabra]
        cant += 1
    
    prom = suma/cant
    print(f"El promedio de {palabra} de todos los países es de {prom}")
    

def submenu_estadisticas(): 
    #En main habrá un solo boton para estadisticas que mostrará un menu en el cual dependiendo del valor 
    #hara una u otra cosa
    
    print("""
            
                        --- MENÚ ESTADÍSTICAS ---
                
                (1) VER PAÍS CON MENOR POBLACIÓN
                (2) VER PAÍS CON MAYOR POBLACIÓN
                (3) VER PROMEDIO DE POBLACIÓN DE LOS PAÍSES
                (4) VER PROMEDIO DE SUPERFICIE DE LOS PAÍSES
            
            """)
    while True:
        try:
            opcion = num_mayor()
            
            if opcion > 4:
                print("ERROR: Valor inválido, intente nuevamente.")
                continue
            break
        except ValueError:
            print("ERROR: Valor inválido, intente nuevamente.")
    return opcion

def match_estadisticas():
    opcion = submenu_estadisticas()
    match opcion:
        case 1:
            pais_mayor_menor_poblacion(listado_paises,opcion)
        case 2:
            pais_mayor_menor_poblacion(listado_paises,opcion)
        case 3:
            promedio(listado_paises,opcion)
        case 4:
            promedio(listado_paises,opcion)




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

