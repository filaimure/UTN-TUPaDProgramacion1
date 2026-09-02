#---------------------------------------------------------------------------------------------------------------#
# TP INTEGRADOR "REPETITIVAS" EJ: 2
# ALUMNO: JANO MONTEROS
# DNI: 45012107
# NOTA: Escribo las variables en ingles porque me gusta como queda :)
#---------------------------------------------------------------------------------------------------------------#
# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Requisitos:
#---------------------------------------------------------------------------------------------------------------#
# 1. Definir credenciales fijas en el código:
# - usuario correcto: "alumno"
# - clave correcta: "python123"
#---------------------------------------------------------------------------------------------------------------#
limit = 1
user_name = input(f"intento {limit}/3 - ingrese su nombre de usuario: ")
password = input(f"Intento {limit}/3 - ingrese su clave de acceso: ")
while (user_name != "jano") or (password != "123456"):
    limit += 1
    print("Contraseña o usuario incorrecto") 
    user_name = input(f"intento {limit}/3 - ingrese su nombre de usuario: ")
    password = input(f"Intento {limit}/3 - ingrese su clave de acceso: ")
#---------------------------------------------------------------------------------------------------------------#
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
#---------------------------------------------------------------------------------------------------------------#
    if (limit == 3) and (user_name != "alumno") and (password != "python123"):
#---------------------------------------------------------------------------------------------------------------#
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#---------------------------------------------------------------------------------------------------------------#
        print("Superaste el maximo de intentos perimitidos: (Cuenta bloqueada)")
        break
#---------------------------------------------------------------------------------------------------------------#
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#---------------------------------------------------------------------------------------------------------------#
if (user_name == "jano") and (password == "123456"):
    print("Menu de usuario")
    print("1. Ver estado de inscripción")
    print("2. Cambiar clave")
    print("3. Mostrar mensaje motivacional")
    print("4. Salir")
    user_selection = input("Opcion numero: ")
    while True:
        if not user_selection.isdigit():
            print("Solo tiene permitido ingresar valores numericos")
        elif int(user_selection) < 1 or int(user_selection) > 4:
            print("Opción inválida o fuera del rango")
        elif int(user_selection) == 4:
            break
#---------------------------------------------------------------------------------------------------------------#
# 1). Ver estado de inscripción (mostrar “Inscripto”)
#---------------------------------------------------------------------------------------------------------------#
        elif int(user_selection) == 1:
            print("-------------------------------")
            print("Usted esta: (I N S C R I P T O)")
            print("-------------------------------")
#---------------------------------------------------------------------------------------------------------------#
# 2). Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#---------------------------------------------------------------------------------------------------------------#
        elif int(user_selection) == 2:
            print("Usted desea cambiar de clave")
            new_password = input("Ingrese su nueva contraseña: ")
            repeat_pass = input("Ingrese otra vez la contraseña: ")
            long_1 = len(new_password)
            while new_password != repeat_pass:
                print("Sus contraseñas no coinciden!")
                new_password = input("Ingrese su nueva contraseña: ")
                repeat_pass = input("Ingrese otra vez la contraseña: ")
                long_1 = len(new_password)
            while int(long_1) < 6: 
                print("Su contraseña no debe tener menos de 6 caracteres.")
                new_password = input("Ingrese su nueva contraseña: ")
                repeat_pass = input("Ingrese otra vez la contraseña: ")
                long_1 = len(new_password)
            if (new_password == repeat_pass) and (int(long_1) >= 6):
                password = new_password
                print("--------------------------------------")
                print("Contraseña cambiada satisfactoriamente")
                print("Nueva contraseña:",password)
                print("--------------------------------------")
#---------------------------------------------------------------------------------------------------------------#
# 3). Mostrar mensaje motivacional (1 frase)
#---------------------------------------------------------------------------------------------------------------#
        elif int(user_selection) == 3:
            print("---------------------------------------------------------------")
            print("No nos atrevemos a hacer muchas cosas por paracer imposibles...")
            print("Pero parecen imposibles exactamente, por no atrevernos a hacerlas")
            print("---------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------------------#
# 4). Salir
#---------------------------------------------------------------------------------------------------------------#
        print("Menu de usuario")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")
        user_selection = input("Opcion numero: ")
           
#---------------------------------------------------------------------------------------------------------------#
# 5. Validación del menú:
# a. Debe ser número (.isdigit())
# b. Debe estar entre 1 y 4
# c. Cambio de clave
#   - La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
#     rechazar.
#---------------------------------------------------------------------------------------------------------------#
