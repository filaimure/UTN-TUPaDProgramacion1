# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Contexto
# Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos:
# Lunes: 4 turnos
# Martes: 3 turnos
# Reglas
# Pedir nombre del operador (solo letras).
# Menú repetitivo hasta salir:
# Reservar turno
# Cancelar turno (por nombre)
# Ver agenda del día
# Ver resumen general
# Cerrar sistema 3. Reservar:
# Elegir día (1=Lunes, 2=Martes).
# Pedir nombre del paciente (solo letras).
# Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
# Guardar en el primer espacio libre (ej. lunes1, lunes2…).
# Cancelar:
# Elegir día. o 	Pedir nombre del paciente (solo letras).
# Si existe, cancelar y dejar el espacio vacío ("").
# Ver agenda del día:
# Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
# Resumen general:
# Turnos ocupados y disponibles por día. o 	Día con más turnos (o empate).
# Restricciones
# No listas, no diccionarios, no sets, no tuplas.
# Se permite usar "" como “vacío”.
# Validaciones con .isalpha() y .isdigit() (sin try/except).

# variables para almacenar los turnos de cada día
global lunes_t1, lunes_t2, lunes_t3, lunes_t4
global martes_t1, martes_t2, martes_t3
global turnos_lunes_ocupados, turnos_martes_ocupados
turnos_lunes_ocupados = 0
turnos_martes_ocupados = 0
lunes_t1 = ""
lunes_t2 = ""
lunes_t3 = ""
lunes_t4 = ""
martes_t1 = ""
martes_t2 = ""
martes_t3 = ""


# Entrada del operador (Requerimiento 1 enunciado)

nombre_operador = input("Ingrese el nombre del operador: ")
while not nombre_operador.isalpha():
    print("Error: el nombre del operador debe contener solo letras.")
    nombre_operador = input("Ingrese el nombre del operador: ")
print(f"Bienvenido, {nombre_operador}.")

# Funciones para el sistema de agenda de turnos


def mostrar_menu() -> None:
    """Muestra el menú de opciones para el sistema de agenda de turnos."""
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema\n")


# Función para reservar un turno


def reservar_turno() -> None:
    """ " Permite reservar un turno ingresando el nombre del paciente y el día. Si el paciente no tiene un turno reservado en ese día, se reserva el primer turno disponible. Si el paciente ya tiene un turno reservado o no hay turnos disponibles, se muestra un mensaje de error."""
    global lunes_t1, lunes_t2, lunes_t3, lunes_t4
    global martes_t1, martes_t2, martes_t3
    dia = input("\nElegir día (1=Lunes, 2=Martes): ")
    while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
        print("Error: ingrese '1' para Lunes o '2' para Martes.")
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
    dia = int(dia)
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    while not nombre_paciente.isalpha():
        print("Error: el nombre debe contener solo letras.")
        nombre_paciente = input("Ingrese el nombre del paciente: ")
    if dia == 1:
        if (
            nombre_paciente == lunes_t1
            or nombre_paciente == lunes_t2
            or nombre_paciente == lunes_t3
            or nombre_paciente == lunes_t4
        ):
            print("Error: el paciente ya tiene un turno reservado el Lunes.")
            return
        if lunes_t1 == "":
            lunes_t1 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Lunes en el Turno 1.")
        elif lunes_t2 == "":
            lunes_t2 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Lunes en el Turno 2.")
        elif lunes_t3 == "":
            lunes_t3 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Lunes en el Turno 3.")
        elif lunes_t4 == "":
            lunes_t4 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Lunes en el Turno 4.")
        else:
            print("No hay turnos disponibles el Lunes.")
    else:
        if (
            nombre_paciente == martes_t1
            or nombre_paciente == martes_t2
            or nombre_paciente == martes_t3
        ):
            print("Error: el paciente ya tiene un turno reservado el Martes.")
            return
        if martes_t1 == "":
            martes_t1 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Martes en el Turno 1.")
        elif martes_t2 == "":
            martes_t2 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Martes en el Turno 2.")
        elif martes_t3 == "":
            martes_t3 = nombre_paciente
            print(f"Turno reservado para {nombre_paciente} el Martes en el Turno 3.")
        else:
            print("No hay turnos disponibles el Martes.")


# Función para cancelar un turno


def cancelar_turno() -> None:
    """ " Permite cancelar un turno ingresando el nombre del paciente y el día. Si el paciente tiene un turno reservado en ese día, se cancela y se deja el espacio vacío (""). Si no se encuentra un turno con ese nombre, se muestra un mensaje de error."""
    global lunes_t1, lunes_t2, lunes_t3, lunes_t4
    global martes_t1, martes_t2, martes_t3
    dia = input("\nElegir día para cancelar (1=Lunes, 2=Martes): ")
    while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
        print("Error: ingrese '1' para Lunes o '2' para Martes.")
        dia = input("Elegir día para cancelar (1=Lunes, 2=Martes): ")
    dia = int(dia)
    nombre_paciente = input("Ingrese el nombre del paciente a cancelar: ")
    while not nombre_paciente.isalpha():
        print("Error: el nombre debe contener solo letras.")
        nombre_paciente = input("Ingrese el nombre del paciente a cancelar: ")
    if dia == 1:
        if nombre_paciente == lunes_t1:
            lunes_t1 = ""
            print(f"Turno cancelado para {nombre_paciente} el Lunes en el Turno 1.")
        elif nombre_paciente == lunes_t2:
            lunes_t2 = ""
            print(f"Turno cancelado para {nombre_paciente} el Lunes en el Turno 2.")
        elif nombre_paciente == lunes_t3:
            lunes_t3 = ""
            print(f"Turno cancelado para {nombre_paciente} el Lunes en el Turno 3.")
        elif nombre_paciente == lunes_t4:
            lunes_t4 = ""
            print(f"Turno cancelado para {nombre_paciente} el Lunes en el Turno 4.")
        else:
            print("No se encontró un turno reservado con ese nombre el Lunes.")
    else:
        if nombre_paciente == martes_t1:
            martes_t1 = ""
            print(f"Turno cancelado para {nombre_paciente} el Martes en el Turno 1.")
        elif nombre_paciente == martes_t2:
            martes_t2 = ""
            print(f"Turno cancelado para {nombre_paciente} el Martes en el Turno 2.")
        elif nombre_paciente == martes_t3:
            martes_t3 = ""
            print(f"Turno cancelado para {nombre_paciente} el Martes en el Turno 3")
        else:
            print("No se encontró un turno reservado con ese nombre el Martes.")


# Función para ver la agenda del día


def ver_agenda_dia() -> None:
    """ " Muestra la agenda del día seleccionado, indicando el nombre del paciente reservado en cada turno o "(libre)" si el turno está vacío."""
    global lunes_t1, lunes_t2, lunes_t3, lunes_t4
    global martes_t1, martes_t2, martes_t3
    dia = input("\nElegir día para ver agenda (1=Lunes, 2=Martes): ")
    while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
        print("Error: ingrese '1' para Lunes o '2' para Martes.")
        dia = input("Elegir día para ver agenda (1=Lunes, 2=Martes): ")
    dia = int(dia)
    if dia == 1:
        print("Agenda del Lunes:")
        print(f"Turno 1: {lunes_t1 if lunes_t1 != '' else '(libre)'}")
        print(f"Turno 2: {lunes_t2 if lunes_t2 != '' else '(libre)'}")
        print(f"Turno 3: {lunes_t3 if lunes_t3 != '' else '(libre)'}")
        print(f"Turno 4: {lunes_t4 if lunes_t4 != '' else '(libre)'}")
    else:
        print("Agenda del Martes:")
        print(f"Turno 1: {martes_t1 if martes_t1 != '' else '(libre)'}")
        print(f"Turno 2: {martes_t2 if martes_t2 != '' else '(libre)'}")
        print(f"Turno 3: {martes_t3 if martes_t3 != '' else '(libre)'}")


# Función para ver el resumen general


def ver_resumen_general() -> None:
    """ " Muestra un resumen general con la cantidad de turnos ocupados y disponibles por día, e indica cuál día tiene más turnos ocupados o si hay un empate."""
    global lunes_t1, lunes_t2, lunes_t3, lunes_t4
    global martes_t1, martes_t2, martes_t3
    global turnos_lunes_ocupados, turnos_martes_ocupados
    turnos_lunes_ocupados = 0
    turnos_martes_ocupados = 0
    if lunes_t1 != "":
        turnos_lunes_ocupados += 1
    if lunes_t2 != "":
        turnos_lunes_ocupados += 1
    if lunes_t3 != "":
        turnos_lunes_ocupados += 1
    if lunes_t4 != "":
        turnos_lunes_ocupados += 1
    if martes_t1 != "":
        turnos_martes_ocupados += 1
    if martes_t2 != "":
        turnos_martes_ocupados += 1
    if martes_t3 != "":
        turnos_martes_ocupados += 1
    print(f"\nResumen General:")
    print(
        f"Lunes: {turnos_lunes_ocupados} turnos ocupados, {4 - turnos_lunes_ocupados} turnos disponibles."
    )
    print(
        f"Martes: {turnos_martes_ocupados} turnos ocupados, {3 - turnos_martes_ocupados} turnos disponibles."
    )
    if turnos_lunes_ocupados > turnos_martes_ocupados:
        print("El día con más turnos ocupados es: Lunes.")
    elif turnos_martes_ocupados > turnos_lunes_ocupados:
        print("El día con más turnos ocupados es: Martes.")
    else:
        print("Ambos días tienen la misma cantidad de turnos ocupados (empate).")


# Función para cerrar el sistema


def cerrar_sistema() -> None:
    """ " Muestra un mensaje de despedida y termina el programa."""
    print("Cerrando el sistema. ¡Hasta luego!")


# Bucle principal del programa

while True:
    print("\nSeleccione una opción: \n")
    mostrar_menu()
    opcion = input("")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: ingrese un número válido entre 1 y 5.")
        opcion = input("Seleccione una opción: ")
    opcion = int(opcion)
    if opcion == 1:
        reservar_turno()
    elif opcion == 2:
        cancelar_turno()
    elif opcion == 3:
        ver_agenda_dia()
    elif opcion == 4:
        ver_resumen_general()
    elif opcion == 5:
        cerrar_sistema()
        break
