from validaciones import num_mayor,texto_vacio,num_no_negativo
from ordenamiento import submenu_match_orden
from crud import cargar_datos,crea_y_añadir_lista
from bucarnombre import buscar_pais
from estadistica import match_estadisticas
from filtrar_paises import f_continente,f_poblacion,f_superficie

def principal():# inicia la creacion y adicion de la lista y luego carga el menú principal
    crea_y_añadir_lista(paises_en_lista())
    listado_paises = cargar_datos()

    opciones()


def paises_en_lista():
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
    return listado_paises

def menu():
    print("""
            
            --- MENÚ PRINCIPAL ---
            (1) Buscar país por nombre
            (2) Filtrar países
            (3) Ordenar países
            (4) Estadísticas
            (5) Salir
            """)

def opciones(): #Menú principal
    while True:
        
        menu()
        while True:
            opcion = num_mayor()
            
            if opcion > 5:
                print("ERROR: Valor inválido, vuelve a intentarlo.")
                continue
            break
        
        match opcion:
            case 1:
                print ("ingresa el nombre del pais que buscas")
                nombre = texto_vacio()
                print (buscar_pais(nombre,paises_en_lista()))
            case 2:
                opciones = input("""
                    (a) Filtro por continente
                    (b) Filtro por poblacion
                    (c) Filtro por superficie
                    """).lower()
                opcion_filtrado(opciones)
            case 3:
                submenu_match_orden()
            case 4:
                match_estadisticas()
            case 5:
                print ("¡Hasta Luego!")
                break

def opcion_filtrado(x):
    match x:
        case "a":
            print ("ingresa un continente")
            continente = texto_vacio()
            if continente in ["america","europa","africa","oceania","asia"]:
                print (f_continente(continente,paises_en_lista()))
            else:
                print (f"ERROR: {continente} no registrado")    
        case "b":
            print ("introduce el minimo numero de poblcion")
            minimo = num_no_negativo()
            print ("introduce el minimo numero de poblcion")
            maximo = num_no_negativo()
            print (f_poblacion(minimo,maximo,paises_en_lista()))
        case "c":
            print ("introduce el minimo tamaño de superficie")
            minimo = num_no_negativo()
            print ("introduce el maximo tamaño de superficie")
            maximo = num_no_negativo()
            print (f_superficie(minimo,maximo,paises_en_lista()))
        case other:
            print ("opcion no valida")
            


if __name__ =="__main__":
    principal()