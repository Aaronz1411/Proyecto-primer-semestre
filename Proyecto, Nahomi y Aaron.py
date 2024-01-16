
#Los primeros with leeran el archivo de claves y patrones obvios para guardarlos en sus respectivos arreglos

with open ("Contraseñas - Proyecto (Fundamentos de Programación SEM202415).txt", "r", encoding="utf-8") as archivo:
    contenido_de_claves = archivo.readlines()
with open ("Patrones obvios de contraseña - Proyecto (Fundamentos de Programación SEM202415).txt", "r", encoding="utf-8") as archivo:
    contenido_de_patrones = archivo.readlines()

#Esta funcion removera los /n del arreglo de claves
def arreglo_de_claves(claves):

    for lineas in range(0, len(claves)):
        if "\n" in claves[lineas]:
            claves[lineas] = claves[lineas].replace("\n", "")
    return claves

#Esta funcion removera los /n del arreglo de patrones obvios
def arreglo_de_patrones(patrones):
    for lineas in range(0, len(patrones)):
        if "\n" in patrones[lineas]:
            patrones[lineas] = patrones[lineas].replace("\n", "")
        
    
    return patrones

def suma_de_puntaje(clave_dada):
    #Guardo en cadenas los caracteres a analizar de cada clave
    minusculas = "qwertyuioplkjhgfdsazxcvbnmñ"
    mayusculas = "QWERTYUIOPLKJHGFDSAZXCVBNMÑ"
    numeros = "1234567890"

    #Estas validaciones indicaran si se ha encontrado un tipo de caracter en la clave, Falso(no se han encontrado), True(se han encontrado)
    validacion_minusculas = False
    validacion_mayusculas = False
    validacion_numeros = False
    validacion_especiales = False
    
    puntaje = 0

    for caracter in range(0, len(clave_dada)):

        if clave_dada[caracter] in minusculas and validacion_minusculas == False:
            puntaje = puntaje + 1
            validacion_minusculas = True

        elif clave_dada[caracter] in mayusculas and validacion_mayusculas == False:
            puntaje = puntaje + 1
            validacion_mayusculas = True

        elif clave_dada[caracter] in numeros and validacion_numeros == False:
            puntaje = puntaje + 1
            validacion_numeros = True

        #Cualquier cosa que no este en las cadenas utilizadas, sera un caracter especial    
        elif clave_dada[caracter]  not in numeros and clave_dada[caracter] not in minusculas and clave_dada[caracter] not in mayusculas:
            
            if validacion_especiales == False:
                puntaje = puntaje + 3
                validacion_especiales = True
            else:
                puntaje = puntaje + 2
        
        
    puntaje = puntaje + len(clave_dada)
    return puntaje 

def resta_de_puntaje(clave_dada):
    patrones = arreglo_de_patrones(contenido_de_patrones)
    puntaje = 0

    #Utilizo el arreglo de patrones para comparar cada patron con la clave dada
    for patron in range(len(patrones)):
        if patrones[patron] in clave_dada:
            
            puntaje = puntaje + 5
            

    return puntaje

#Utilizo las dos anteriores funcionas para calcular el puntaje de cada clave
def calcular_puntaje_seguridad(clave_dada):
    puntaje_final = suma_de_puntaje(clave_dada) - resta_de_puntaje(clave_dada)
    return puntaje_final

def clasificacion_de_seguridad(puntaje_final):
    categoria = ""
    if puntaje_final <= 15:
        categoria = "Debil"
    elif puntaje_final > 15 and puntaje_final <= 20:
        categoria = "Moderada"
    elif puntaje_final > 20 and puntaje_final <= 35:
        categoria = "Buena"
    elif puntaje_final > 35 and puntaje_final <= 100:
        categoria = "Excelente"
    elif puntaje_final > 100:
        categoria = "Impenetrable"
    return categoria

def arreglo_nuevo():
    
    #La funcion de clasificacion y calculo de puntaje, utilizaran cada elemento del arreglo de claves para modificar el propio arreglo
    claves = arreglo_de_claves(contenido_de_claves)
    for clave in range(len(claves)):
        puntaje = calcular_puntaje_seguridad(claves[clave])
        categoria = clasificacion_de_seguridad(puntaje)
        claves[clave] = claves[clave] + "|" + categoria + "|" + str(puntaje)

def ordenamiento_de_claves(nuevo_arreglo):
    
    for i in range(len(nuevo_arreglo)):
        for j in range(len(nuevo_arreglo) -1 -i):

            puntaje1 = ""
            puntaje2 = ""

            #Los siguientes for,  detectaran el puntaje de cada contraseña en el nuevo arreglo de claves 
            for caracter_1 in range(len(nuevo_arreglo[j]) -1, -1, -1):
                if nuevo_arreglo[j][caracter_1]  != "|":
                    puntaje1 = nuevo_arreglo[j][caracter_1] + puntaje1
                else:
                    break

            for caracter_2 in range(len(nuevo_arreglo[j + 1]) -1 , -1, -1):
                if nuevo_arreglo[j + 1][caracter_2]  != "|":
                    puntaje2 = nuevo_arreglo[j + 1][caracter_2] + puntaje2
                else:
                    break
            
            #Los puntajes al ser datos string, deben ser cambiados a enteros para su comparion 
            puntaje1 = int(puntaje1)
            puntaje2 = int(puntaje2)
            

            if puntaje1 < puntaje2:
                aux = nuevo_arreglo[j]
                nuevo_arreglo[j] = nuevo_arreglo[j + 1]
                nuevo_arreglo[j + 1] = aux
    return nuevo_arreglo
    
def nuevo_archivo(arreglo_final):
    with open ("experimento.txt", "w", encoding="UTF-8") as archivo:
        archivo.write("") 
    with open ("experimento.txt", "a", encoding="UTF-8") as archivo:
        for i in range(len(arreglo_final)):
            archivo.write(f"{arreglo_final[i]}\n")


arreglo_nuevo()
arreglo_ordenado = ordenamiento_de_claves(contenido_de_claves)
nuevo_archivo(arreglo_ordenado)