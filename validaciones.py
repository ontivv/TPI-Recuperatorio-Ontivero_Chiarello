def texto_vacio(): # t es un string
    while True:
        texto = input().lower().strip()
        if  len(texto) > 0:
            return texto

def texto_existente(texto,lista):
    for dic in lista:
        if  texto in dic["nombre"]:
            return True
    return False

def numero_entero():
    while True:
        try:
            x = int(input(""))
            return x
        except ValueError:
            print (f"ERROR:{x} no valido")

def num_mayor():
    while True:
        try:
            x = int(input(""))
            if x > 0:
                return x
            else:
                print("ERROR: Valor inválido, intente nuevamente.")
        except ValueError:
            print("ERROR: Valor inválido, intente nuevamente.")

def num_no_negativo():
    while True:
        try:
            x = int(input(""))
            if x >= 0:
                return x
            else:
                print("ERROR: Valor inválido, intente nuevamente.")
        except ValueError:
            print("ERROR: Valor inválido, intente nuevamente.")