# LISTA PRINCIPAL

paises = []

# FUNCION AGREGAR PAIS

def agregar_pais():

    print("\n--- AGREGAR PAIS ---")

    nombre = input("Ingrese nombre: ")

    while nombre == "":
        print("Error. El nombre no puede estar vacio")
        nombre = input("Ingrese nombre: ")

    poblacion = input("Ingrese poblacion: ")

    while poblacion.isdigit() == False:
        print("Error. Debe ingresar numeros")
        poblacion = input("Ingrese poblacion: ")

    poblacion = int(poblacion)

    superficie = input("Ingrese superficie: ")

    while superficie.isdigit() == False:
        print("Error. Debe ingresar numeros")
        superficie = input("Ingrese superficie: ")

    superficie = int(superficie)

    continente = input("Ingrese continente: ")

    while continente == "":
        print("Error. El continente no puede estar vacio")
        continente = input("Ingrese continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("Pais agregado correctamente")


# FUNCION MOSTRAR PAISES

def mostrar_paises():

    print("\n--- LISTA DE PAISES ---")

    if len(paises) == 0:
        print("No hay paises cargados")

    else:

        for pais in paises:
            print("----------------------")
            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

# FUNCION BUSCAR PAIS

def buscar_pais():

    print("\n--- BUSCAR PAIS ---")

    busqueda = input("Ingrese nombre a buscar: ").lower()

    encontrado = False

    for pais in paises:

        if busqueda in pais["nombre"].lower():

            print("----------------------")
            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

            encontrado = True

    if encontrado == False:
        print("No se encontraron paises")


# FUNCION ACTUALIZAR PAIS


def actualizar_pais():

    print("\n--- ACTUALIZAR PAIS ---")

    nombre_busqueda = input("Ingrese nombre del pais: ").lower()

    encontrado = False

    for pais in paises:

        if nombre_busqueda == pais["nombre"].lower():

            nueva_poblacion = input("Ingrese nueva poblacion: ")

            while nueva_poblacion.isdigit() == False:
                print("Error. Debe ingresar numeros")
                nueva_poblacion = input("Ingrese nueva poblacion: ")

            nueva_poblacion = int(nueva_poblacion)

            nueva_superficie = input("Ingrese nueva superficie: ")

            while nueva_superficie.isdigit() == False:
                print("Error. Debe ingresar numeros")
                nueva_superficie = input("Ingrese nueva superficie: ")

            nueva_superficie = int(nueva_superficie)

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            print("Pais actualizado correctamente")

            encontrado = True

    if encontrado == False:
        print("Pais no encontrado")


# FILTRAR POR CONTINENTE


def filtrar_continente():

    print("\n--- FILTRAR POR CONTINENTE ---")

    continente = input("Ingrese continente: ").lower()

    encontrado = False

    for pais in paises:

        if continente == pais["continente"].lower():

            print("----------------------")
            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

            encontrado = True

    if encontrado == False:
        print("No hay paises en ese continente")


# FILTRAR POR POBLACION


def filtrar_poblacion():

    print("\n--- FILTRAR POR POBLACION ---")

    minimo = input("Ingrese poblacion minima: ")

    while minimo.isdigit() == False:
        print("Error. Debe ingresar numeros")
        minimo = input("Ingrese poblacion minima: ")

    minimo = int(minimo)

    maximo = input("Ingrese poblacion maxima: ")

    while maximo.isdigit() == False:
        print("Error. Debe ingresar numeros")
        maximo = input("Ingrese poblacion maxima: ")

    maximo = int(maximo)

    encontrado = False

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            print("----------------------")
            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

            encontrado = True

    if encontrado == False:
        print("No se encontraron paises")

# FILTRAR POR SUPERFICIE

def filtrar_superficie():

    print("\n--- FILTRAR POR SUPERFICIE ---")

    minimo = input("Ingrese superficien minima: ")

    while minimo.isdigit() == False:
        print("Error. Debe ingresar numeros")
        minimo = input("Ingrese superficie minima: ")

    minimo = int(minimo)

    maximo = input("Ingrese superficie maxima: ")

    while maximo.isdigit() == False:
        print("Error. Debe ingresar numeros")
        maximo = input("Ingrese superficie maxima: ")

    maximo = int(maximo)

    encontrado = False

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            print("----------------------")
            print("Nombre:", pais["nombre"])
            print("Poblacion:", pais["poblacion"])
            print("Superficie:", pais["superficie"])
            print("Continente:", pais["continente"])

            encontrado = True

    if encontrado == False:
        print("No se encontraron paises")

# ORDENAR POR NOMBRE

def ordenar_nombre():

    print("\n--- ORDENAR POR NOMBRE ---")

    lista_ordenada = paises.copy()

    for i in range(len(lista_ordenada)):

        for j in range(i + 1, len(lista_ordenada)):

            if lista_ordenada[i]["nombre"] > lista_ordenada[j]["nombre"]:

                auxiliar = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[j]
                lista_ordenada[j] = auxiliar

    for pais in lista_ordenada:

        print("----------------------")
        print("Nombre:", pais["nombre"])
        print("Poblacion:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])


# ORDENAR POR POBLACION


def ordenar_poblacion():

    print("\n--- ORDENAR POR POBLACION ---")

    opcion = input("1- Ascendente | 2- Descendente: ")

    lista_ordenada = paises.copy()

    for i in range(len(lista_ordenada)):

        for j in range(i + 1, len(lista_ordenada)):

            if opcion == "1":

                if lista_ordenada[i]["poblacion"] > lista_ordenada[j]["poblacion"]:

                    auxiliar = lista_ordenada[i]
                    lista_ordenada[i] = lista_ordenada[j]
                    lista_ordenada[j] = auxiliar

            elif opcion == "2":

                if lista_ordenada[i]["poblacion"] < lista_ordenada[j]["poblacion"]:

                    auxiliar = lista_ordenada[i]
                    lista_ordenada[i] = lista_ordenada[j]
                    lista_ordenada[j] = auxiliar

    for pais in lista_ordenada:

        print("----------------------")
        print("Nombre:", pais["nombre"])
        print("Poblacion:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])

# ORDENAR POR POBLACION

def ordenar_superficie():

    print("\n--- ORDENAR POR SUPERFICIE ---")

    opcion = input("1- Ascendente | 2- Descendente: ")

    lista_ordenada = paises.copy()

    for i in range(len(lista_ordenada)):

        for j in range(i + 1, len(lista_ordenada)):

            if opcion == "1":

                if lista_ordenada[i]["superficie"] > lista_ordenada[j]["superficie"]:

                    auxiliar = lista_ordenada[i]
                    lista_ordenada[i] = lista_ordenada[j]
                    lista_ordenada[j] = auxiliar

            elif opcion == "2":

                if lista_ordenada[i]["superficie"] < lista_ordenada[j]["superficie"]:

                    auxiliar = lista_ordenada[i]
                    lista_ordenada[i] = lista_ordenada[j]
                    lista_ordenada[j] = auxiliar

    for pais in lista_ordenada:

        print("----------------------")
        print("Nombre:", pais["nombre"])
        print("Poblacion:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])


# ESTADISTICAS


def mostrar_estadisticas():

    print("\n--- ESTADISTICAS ---")

    if len(paises) == 0:
        print("No hay paises cargados")

    else:

        mayor_poblacion = paises[0]
        menor_poblacion = paises[0]

        suma_poblacion = 0
        suma_superficie = 0

        continentes = {}

        for pais in paises:

            # MAYOR POBLACION
            if pais["poblacion"] > mayor_poblacion["poblacion"]:
                mayor_poblacion = pais

            # MENOR POBLACION
            if pais["poblacion"] < menor_poblacion["poblacion"]:
                menor_poblacion = pais

            # SUMAS
            suma_poblacion += pais["poblacion"]
            suma_superficie += pais["superficie"]

            # CONTINENTES
            continente = pais["continente"]

            if continente in continentes:
                continentes[continente] += 1

            else:
                continentes[continente] = 1

        promedio_poblacion = suma_poblacion / len(paises)
        promedio_superficie = suma_superficie / len(paises)

        print("\nPais con mayor poblacion:")
        print(mayor_poblacion["nombre"])

        print("\nPais con menor poblacion:")
        print(menor_poblacion["nombre"])

        print("\nPromedio de poblacion:")
        print(promedio_poblacion)

        print("\nPromedio de superficie:")
        print(promedio_superficie)

        print("\nCantidad de paises por continente:")

        for continente in continentes:
            print(continente, ":", continentes[continente]) 


# MENU PRINCIPAL


while True:

    print("\n========= MENU =========")
    print("1. Agregar pais")
    print("2. Mostrar paises")
    print("3. Buscar pais")
    print("4. Actualizar pais")
    print("5. Filtrar por continente")
    print("6. Filtrar por poblacion")
    print("7. Filtrar por superficie")
    print("8. Ordenar por nombre")
    print("9. Ordenar por poblacion")
    print("10. Ordenar por superficie")
    print("11. Mostrar estadisticas")
    print("12. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_pais()

    elif opcion == "2":
        mostrar_paises()

    elif opcion == "3":
        buscar_pais()

    elif opcion == "4":
        actualizar_pais()

    elif opcion == "5":
        filtrar_continente()

    elif opcion == "6":
        filtrar_poblacion()

    elif opcion == "7":
        filtrar_superficie()

    elif opcion == "8":
        ordenar_nombre()

    elif opcion == "9":
        ordenar_poblacion()

    elif opcion == "10":
        ordenar_superficie()

    elif opcion == "11":
        mostrar_estadisticas()

    elif opcion == "12":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")