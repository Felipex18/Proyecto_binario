# Función que permite convertir de texto a binario

# Esta función toma un texto como entrada, lo codifica 
# en una secuencia de bytes utilizando UTF-8, y luego convierte 
# cada byte en una cadena binaria de 8 bits, devolviendo la cadena
# binaria completa.
def texto_a_binario(texto):
    bytes_texto = texto.encode('utf-8')
    binario = ' '.join(format(byte, '08b') for byte in bytes_texto)
    return binario

# Función que permite convertir de binario a texto

# Esta función toma una cadena binaria como entrada,
# elimina cualquier espacio entre los bytes,
# divide la cadena binaria en segmentos de 8 bits,
# convierte cada segmento en un byte, y luego decodifica
# la secuencia de bytes resultante en texto utilizando UTF-8.
def binario_a_texto(binario):
    binario_sin_espacios = binario.replace(' ', '')
    segmentos = [binario_sin_espacios[i:i+8] for i in range(0, len(binario_sin_espacios), 8)]
    bytes_texto = bytes(int(segmento, 2) for segmento in segmentos)
    texto = bytes_texto.decode('utf-8')
    return texto

# Función que permite hacer el conteo de una letra en especial usando búsqueda binaria

# Esta función toma un texto como entrada y convierte todas las letras
# a minúsculas para un conteo uniforme. Luego cuenta la cantidad de
# apariciones de cada letra y almacena estos conteos en una lista de tuplas
# ordenada. Solicita al usuario una letra para buscar y muestra cuántas veces 
# aparece esa letra en el texto utilizando búsqueda binaria.
def contar_letras(texto):
    texto = texto.lower()
    contador = {}
    for letra in texto:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    lista_contador = sorted(contador.items())

    def busqueda_binaria(lista, objetivo):
        inicio = 0
        fin = len(lista) - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if lista[medio][0] == objetivo:
                return medio
            elif lista[medio][0] < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1

    letra_a_buscar = input("Ingrese la letra a buscar: ").lower()
    indice = busqueda_binaria(lista_contador, letra_a_buscar)
    if indice != -1:
        print(f"La letra '{letra_a_buscar}' aparece {lista_contador[indice][1]} veces en el texto.")
    else:
        print(f"La letra '{letra_a_buscar}' no se encuentra en el texto.")

# Función que permite mostrar el menú que utiliza el usuario

# Esta función muestra un menú principal con opciones para convertir
# texto a binario, convertir binario a texto, o salir del programa.
# Dependiendo de la opción seleccionada por el usuario, se llama a la
# función correspondiente y se muestra un submenú después de ejecutar
# una conversión.
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Convertir texto a binario")
        print("2. Convertir binario a texto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            texto_original = input("Ingrese el texto a convertir: ")
            binario_resultante = texto_a_binario(texto_original)
            print("Texto en binario:", binario_resultante)
            submenu(texto_original)
        elif opcion == '2':
            binario = input("Ingrese el binario a convertir: ")
            texto_recuperado = binario_a_texto(binario)
            print("Texto recuperado:", texto_recuperado)
            submenu(texto_recuperado)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Función que permite mostrar el segundo menú que aparece después de ejecutar alguna función principal

# Esta función muestra un submenú con opciones para buscar una letra específica en el texto,
# regresar al menú principal, o salir del programa. Dependiendo de la opción seleccionada,
# se llama a la función correspondiente o se realiza la acción indicada.
def submenu(texto):
    while True:
        print("\n--- Submenú ---")
        print("1. Desea buscar una letra especifica")
        print("2. Regresar al menú principal")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            contar_letras(texto)
        elif opcion == '2':
            break
        elif opcion == '3':
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida, intente de nuevo.")

# Al correr el código se llama la función del menú principal
menu_principal()
