# TP INTEGRADOR "REPETITIVAS" EJ: 3
# ALUMNO: JANO MONTEROS
# DNI: 45012107
# NOTA: Escribo las variables en ingles porque me gusta como queda :)

#---------------------------------------------------------------------------------------------------------------#
# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Contexto:
# Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos:
# • Lunes: 4 turnos.
# • Martes: 3 turnos.
# Reglas:
#---------------------------------------------------------------------------------------------------------------#
# 1. Pedir nombre del operador (solo letras).
#---------------------------------------------------------------------------------------------------------------#
# 2. Menú repetitivo hasta salir:
#         - 1. Reservar turno
#         - 2. Cancelar turno (por nombre)
#         - 3. Ver agenda del día
#         - 4. Ver resumen general
#         - 5. Cerrar sistema
#---------------------------------------------------------------------------------------------------------------#
# 2.1. Reservar:
#    - Elegir día (1=Lunes, 2=Martes).
#    - Pedir nombre del paciente (solo letras).
#    - Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#    - Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#---------------------------------------------------------------------------------------------------------------#
# 2.2. Cancelar:
#    - Elegir día.
#    - Pedir nombre del paciente (solo letras).
#    - Si existe, cancelar y dejar el espacio vacío ("").
#---------------------------------------------------------------------------------------------------------------#
# 2.3. Ver agenda del día:
#    - Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
#---------------------------------------------------------------------------------------------------------------#
# 2.4. Resumen general:
#    - Turnos ocupados y disponibles por día.
#    - Día con más turnos (o empate).
# Restricciones
# • ❌ No listas, no diccionarios, no sets, no tuplas.
# • ✅ Se permite usar "" como “vacío”.
# • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).
#----------------(DIAS/TURNOS VACIOS)----------------------------------------------------------------------------#
monday_t1 = ""
monday_t2 = ""
monday_t3 = ""
monday_t4 = ""
tuesday_t1 = ""
tuesday_t2 = ""
tuesday_t3 = ""
#--------------(INGRESO OPERADOR)-------------------------------------------------------------------------------#
operator_name = input("Operador designado, ingrese su nombre: ").strip()
while not operator_name.replace(" ", "").isalpha():
    print("Su nombre solo debe contener letras.")
    operator_name = input("Ingrese su nombre: ").strip()
#--------------(MENU INICIAL)-----------------------------------------------------------------------------------#
print("Bienvenido operador:",operator_name)
print("Agenda de turnos")
print("1. Reservar turno")
print("2. Cancelar turno")
print("3. Ver agenda del día")
print("4. Ver resumen general")
print("5. Cerrar sistema")
user_selection = input("Opcion numero: ")
#-----------(VERIFICACION INGRESO CORRECTO)---------------------------------------------------------------------#
while not user_selection.isdigit():
    print("Solo tiene permitido ingresar valores numericos")
    user_selection = input("Opcion numero: ")
#-----------(VERIFICACION DE SALIDA/EXCESO)---------------------------------------------------------------------#
while int(user_selection) != 5:
    if int(user_selection) < 1 or int(user_selection) > 5:
        print("Opción inválida o fuera del rango")
        user_selection = input("Opcion numero: ")
#-----------(MENU DE RESERVA)-----------------------------------------------------------------------------------#      
    elif int(user_selection) == 1:
        print("(Reserva de turnos)")
        print("Seleccione un dia:")
        print("1. Lunes")
        print("2. Martes")
        day_selection = input("Cual prefiere? (1 o 2): ")
        while not day_selection.isdigit():
            print("Solo tiene permitido ingresar numeros")
            day_selection = input("Cual prefiere? (1 o 2): ")
        while int(day_selection) != 1 and int(day_selection) != 2:
            print("Opción inválida o fuera del rango")
            day_selection = input("Cual prefiere? (1 o 2): ")
#-----------(TURNO LUNES)---------------------------------------------------------------------------------------#
        if int(day_selection) == 1:
            patient_name = input("Ingrese el nombre del paciente: ").strip()
            while not patient_name.replace(" ", "").isalpha():
                print("El nombre solo debe contener letras.")
                patient_name = input("Re-ingrese el nombre del paciente: ").strip()
#-----------(VERIFICACION/NOTIFICACION TURNO OCUPADO)-----------------------------------------------------------#
            if (patient_name == monday_t1 or patient_name == monday_t2 or patient_name == monday_t3 or patient_name == monday_t4):
                print("Turno ocupado")
#-----------(VERIFICACION DE LIBRE)----------------------------------------------------------------------------#
            elif monday_t1 == "":
                monday_t1 = patient_name
                print("Turno asignado exitosamente")
            elif monday_t2 == "":
                monday_t2 = patient_name
                print("Turno asignado exitosamente")
            elif monday_t3 == "":
                monday_t3 = patient_name
                print("Turno asignado exitosamente")
            elif monday_t4 == "":
                monday_t4 = patient_name
                print("Turno asignado exitosamente")
#------------(NOTIFICACION DE SIN TURNOS)----------------------------------------------------------------------#
            else: 
                print("Se encuentran ocupados todos los turnos del dia LUNES")
#------------(TURNO MARTES)---------------------------------------------------------------------------------- --#
        elif int(day_selection) == 2:
            patient_name = input("Ingrese el nombre del paciente: ").strip()
            while not patient_name.replace(" ", "").isalpha():
                print("El nombre solo debe contener letras.")
                patient_name = input("Re-ingrese el nombre del paciente: ").strip()
#------------(VERIFICACION/NOTIFICACION TURNO OCUPADO)----------------------------------------------------------#
            if (patient_name == tuesday_t1 or patient_name == tuesday_t2 or patient_name == tuesday_t3):
                print("Turno ocupado")
#------------(VERIFICACION DE LIBRE)----------------------------------------------------------------------------#
            elif tuesday_t1 == "":
                tuesday_t1 = patient_name
                print("Turno asignado exitosamente")
            elif tuesday_t2 == "":
                tuesday_t2 = patient_name
                print("Turno asignado exitosamente")
            elif tuesday_t3 == "":
                tuesday_t3 = patient_name
                print("Turno asignado exitosamente")
#------------(NOTIFICACION DE SIN TURNOS)----------------------------------------------------------------------#
            else: 
                print("Se encuentran ocupados todos los turnos del dia MARTES")
#------------(MENU DE CANCELACION)-----------------------------------------------------------------------------#
    elif int(user_selection) == 2:
        print("(Cancelacion de turnos)")
        print("Seleccione el dia:")
        print("1. Lunes")
        print("2. Martes")
        day_selection = input("A que dia corresponde el turno? (1 o 2): ")
        while not day_selection.isdigit():
            print("Solo tiene permitido ingresar numeros")
            day_selection = input("A que dia corresponde el turno? (1 o 2): ")
        while int(day_selection) != 1 and int(day_selection) != 2:
            print("Opción inválida o fuera del rango")
            day_selection = input("De que dia precisa ver los turnos? (1 o 2): ")
#-----------(CANCELACION TURNO LUNES)---------------------------------------------------------------------------#
        if int(day_selection) == 1:
            patient_name = input("Ingrese el nombre del paciente: ").strip()
            while not patient_name.replace(" ", "").isalpha():
                print("El nombre solo debe contener letras.")
                patient_name = input("Re-ingrese el nombre del paciente: ").strip()
            if patient_name == monday_t1:
                monday_t1 = ""
                print("Turno eliminado exitosamente")
            elif patient_name == monday_t2:
                monday_t2 = ""
                print("Turno eliminado exitosamente")
            elif patient_name == monday_t3:
                monday_t3 = ""
                print("Turno eliminado exitosamente")
            elif patient_name == monday_t4:
                monday_t4 = ""
                print("Turno eliminado exitosamente")
            else:
                print("El paciente no tiene turno asignado")
#-----------(CANCELACION TURNO MARTES)---------------------------------------------------------------------------#
        elif int(day_selection) == 2:
            patient_name = input("Ingrese el nombre del paciente: ").strip()
            while not patient_name.replace(" ", "").isalpha():
                print("El nombre solo debe contener letras.")
                patient_name = input("Re-ingrese el nombre del paciente: ").strip()
            if patient_name == tuesday_t1:
                tuesday_t1 = ""
                print("Turno eliminado exitosamente")
            elif patient_name == tuesday_t2:
                tuesday_t2 = ""
                print("Turno eliminado exitosamente")
            elif patient_name == tuesday_t3:
                tuesday_t3 = ""
                print("Turno eliminado exitosamente")
            else:
                print("El paciente no tiene turno asignado")
    elif int(user_selection) == 3:
        print("Agenda del dia")
        print("Seleccione el dia:")
        print("1. Lunes")
        print("2. Martes")
        day_selection = input("De que dia precisa ver los turnos? (1 o 2): ")
        while int(day_selection) < 1 or int(day_selection) > 2:
            print("Opción inválida o fuera del rango")
            day_selection = input("De que dia precisa ver los turnos? (1 o 2): ")
        while not day_selection.isdigit():
            print("Solo tiene permitido ingresar numeros")
            day_selection = input("A que dia corresponde el turno? (1 o 2): ")
        if int(day_selection) == 1:
            print("#---------------------#")
            print("#----Turnos: LUNES----#")
            print("#---------------------#")
            if monday_t1 != "":
                print("Turno 1:",monday_t1)
            elif monday_t1 == "":
                print("Turno 1: LIBRE")
            if monday_t2 != "":
                print("Turno 2:",monday_t2)
            elif monday_t2 == "":
                print("Turno 2: LIBRE")
            if monday_t3 != "":
                print("Turno 3:",monday_t3)
            elif monday_t3 == "":
                print("Turno 3: LIBRE")
            if monday_t4 != "":
                print("Turno 4:",monday_t4)
            elif monday_t4 == "":
                print("Turno 4: LIBRE")
        elif int(day_selection) == 2:
            print("#----------------------#")
            print("#----Turnos: MARTES----#")
            print("#----------------------#")
            if tuesday_t1 != "":
                print("Turno 1:",tuesday_t1)
            elif tuesday_t1 == "":
                print("Turno 1: LIBRE")
            if tuesday_t2 != "":
                print("Turno 2:",tuesday_t2)
            elif tuesday_t2 == "":
                print("Turno 2: LIBRE")
            if tuesday_t3 != "":
                print("Turno 3:",tuesday_t3)
            elif tuesday_t3 == "":
                print("Turno 3: LIBRE")
#--------------------------------------------------------------------------------------------------------------#
    elif int(user_selection) == 4:
        print("Resumen general")
        print("#---------------------#")
        print("#------Dia LUNES------#")
        print("#---------------------#")
        if monday_t1 != "":
            print("Turno 1:",monday_t1)
        elif monday_t1 == "":
            print("Turno 1: LIBRE")
        if monday_t2 != "":
            print("Turno 2:",monday_t2)
        elif monday_t2 == "":
            print("Turno 2: LIBRE")
        if monday_t3 != "":
            print("Turno 3:",monday_t3)
        elif monday_t3 == "":
            print("Turno 3: LIBRE")
        if monday_t4 != "":
            print("Turno 4:",monday_t4)
        elif monday_t4 == "":
            print("Turno 4: LIBRE")
        print("#---------------------#")
        print("#------Dia MARTES------#")
        print("#---------------------#")
        if tuesday_t1 != "":
            print("Turno 1:",tuesday_t1)
        elif tuesday_t1 == "":
            print("Turno 1: LIBRE")
        if tuesday_t2 != "":
            print("Turno 2:",tuesday_t2)
        elif tuesday_t2 == "":
            print("Turno 2: LIBRE")
        if tuesday_t3 != "":
            print("Turno 3:",tuesday_t3)
        elif tuesday_t3 == "":
            print("Turno 3: LIBRE")
#-------------(DIA MAS COMPLETO)-------------------------------------------------------------------------------#
        monday_count = 0
        tuesday_count = 0
        if monday_t1 != "":
            monday_count += 1
        if monday_t2 != "":
            monday_count += 1
        if monday_t3 != "":
            monday_count += 1
        if monday_t4 != "":
            monday_count += 1
#--------------------------------------------------------------------------------------------------------------#
        if tuesday_t1 != "":
            tuesday_count += 1
        if tuesday_t2 != "":
            tuesday_count += 1
        if tuesday_t3 != "":
            tuesday_count += 1
        if monday_count > tuesday_count:
            print("#------------------------------------------------#")
            print("El dia LUNES tuvo mas pascientes que el dia MARTES")
            print("#------------------------------------------------#")
        elif tuesday_count > monday_count:
            print("#------------------------------------------------#")
            print("El dia MARTES tuvo mas pascientes que el dia LUNES")
            print("#------------------------------------------------#")
        else:
            print("#----------------------------------------------------#")
            print("Ambos dias tienen la misma cantidad de pacientes")
            print("#----------------------------------------------------#")
#-------------(MENU INICIAL)-------------------------------------------------------------------------------------#
    print("Agenda de turnos")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    user_selection = input("Opcion numero: ")
#------------(VERIFICACION INGRESO CORRECTO)--------------------------------------------------------------------#
    while not user_selection.isdigit():
        print("Solo tiene permitido ingresar valores numericos")
        user_selection = input("Opcion numero: ")
#------------(VERIFICACION DE SALIDA/EXCESO)--------------------------------------------------------------------#
    while int(user_selection) < 1 or int(user_selection) > 5:
        print("Opción inválida o fuera del rango")
        user_selection = input("Opcion numero: ")
#------------(MENSAJE AL SALIR)---------------------------------------------------------------------------------#
if int(user_selection) == 5:
    print("Cerrando el sistema...")
    print("Hasta pronto!")
#---------------------------------------------------------------------------------------------------------------#

