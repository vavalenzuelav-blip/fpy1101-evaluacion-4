def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Opción inválida.")
        except:
            print("Opción inválida.")


def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True


def validar_copias(copias):
    try:
        copias = int(copias)
        if copias >= 0:
            return True
        else:
            return False
    except:
        return False


def validar_prestamo(prestamo):
    try:
        prestamo = int(prestamo)
        if prestamo > 0:
            return True
        else:
            return False
    except:
        return False


def agregar_libro(lista):
    titulo = input("Ingrese el título: ")

    if validar_titulo(titulo) == False:
        print("El título es inválido.")
        return

    copias = input("Ingrese la cantidad de copias: ")

    if validar_copias(copias) == False:
        print("La cantidad de copias es inválida.")
        return

    prestamo = input("Ingrese el período de préstamo: ")

    if validar_prestamo(prestamo) == False:
        print("El período de préstamo es inválido.")
        return

    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias),
        "prestamo": int(prestamo),
        "disponible": False
    }

    lista.append(libro)

    print("Libro agregado correctamente.")


def buscar_libro(lista, titulo):

    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i

    return -1


def actualizar_disponibilidad(lista):

    for i in range(len(lista)):
        if lista[i]["copias"] >= 1:
            lista[i]["disponible"] = True
        else:
            lista[i]["disponible"] = False


def mostrar_libros(lista):

    actualizar_disponibilidad(lista)

    print("=== LISTA DE LIBROS ===")

    if len(lista) == 0:
        print("No hay libros registrados.")
        return

    for i in range(len(lista)):

        print("Título:", lista[i]["titulo"])
        print("Copias:", lista[i]["copias"])
        print("Préstamo:", lista[i]["prestamo"])

        if lista[i]["disponible"] == True:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN COPIAS")

        print("-----------------------------")


libros = []

while True:

    mostrar_menu()

    opcion = leer_opcion()

    if opcion == 1:

        agregar_libro(libros)

    elif opcion == 2:

        titulo = input("Ingrese el título del libro: ")

        posicion = buscar_libro(libros, titulo)

        if posicion == -1:
            print("El libro no se encuentra registrado.")
        else:
            print("Posición:", posicion)
            print("Título:", libros[posicion]["titulo"])
            print("Copias:", libros[posicion]["copias"])
            print("Préstamo:", libros[posicion]["prestamo"])

            if libros[posicion]["disponible"] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: SIN COPIAS")

    elif opcion == 3:

        titulo = input("Ingrese el título del libro a eliminar: ")

        posicion = buscar_libro(libros, titulo)

        if posicion == -1:
            print("El libro '" + titulo + "' no se encuentra registrado.")
        else:
            del libros[posicion]
            print("Libro eliminado correctamente.")

    elif opcion == 4:

        actualizar_disponibilidad(libros)

        print("Disponibilidad actualizada.")

    elif opcion == 5:

        mostrar_libros(libros)

    elif opcion == 6:

        print("Gracias por usar el sistema. Vuelva pronto.")
        break