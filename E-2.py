# Ejercicio 2  — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Requisitos
# Definir credenciales fijas en el código: o 	usuario correcto: "alumno" o 	clave correcta: "python123"
# Permitir máximo 3 intentos para ingresar usuario y clave.
# Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
# Ver estado de inscripción (mostrar “Inscripto”)
# Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
# Mostrar mensaje motivacional (1 frase)
# Salir
# Validación del menú: o 	Debe ser número (.isdigit()) o 	Debe estar entre 1 y 4
# Cambio de clave
# • 	La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.
# Salida esperada
# Intento 1/3 - Usuario: alumno
# Clave: xxx
# Error: credenciales inválidas.
# Intento 2/3 - Usuario: alumno
# Clave: python123 Acceso concedido.
# 1) Estado  2) Cambiar clave  3) Mensaje  4) Salir
# Opción: a
# Error: ingrese un número válido.
# Opción: 5
# Error: opción fuera de rango.
# Opción: 2
# Nueva clave: 123
# Error: mínimo 6 caracteres.

# Creación del programa de acceso al campus y menú seguro
# Definición de credenciales fijas
user_name_correct = "alumno"
password_correct = "python123"
# Intentos máximos para ingresar usuario y clave
intentos = 3
# Bucle principal para el login
while not intentos == 0:
    user_name_input = input("Usuario: ")
    while not user_name_input.isalpha():
        print("Error: el usuario debe contener solo letras.")
        user_name_input = input("Usuario: ")
    password_input = input("Clave: ")
    # Validación de credenciales
    if user_name_input == user_name_correct and password_input == password_correct:
        print("Acceso concedido.")
        # Menú repetitivo hasta elegir salir
        while True:
            print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
            opcion = input("Opción: ")
            # Validación del menú
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
                print("Error: ingrese un número válido entre 1 y 4.")
                continue
            # Procesamiento de la opción seleccionada
            opcion = int(opcion)
            # Mostrar estado de inscripción
            if opcion == 1:
                print("Inscripto")
            elif opcion == 2:
                # Cambio de clave con validación de longitud y confirmación
                while True:
                    nueva_clave = input("Nueva clave: ")
                    while not len(nueva_clave) > 5:
                        print("Error: mínimo 6 caracteres.")
                        nueva_clave = input("Nueva clave: ")
                    confirmacion = input("Confirmar clave: ")
                    # Validación de coincidencia de claves
                    if nueva_clave != confirmacion:
                        print("Error: las claves no coinciden.")
                        continue
                    password_correct = nueva_clave
                    print("Clave cambiada exitosamente.")
                    break
            # Mensaje motivacional
            elif opcion == 3:
                print("¡Sigue adelante, estás haciendo un gran trabajo!")
            # Salir del sistema
            elif opcion == 4:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
        break
    # Si las credenciales son incorrectas, se resta un intento y se muestra el error
    else:
        intentos -= 1
        print(f"Error: credenciales inválidas. Intento {3 - intentos}/3")
        if intentos == 0:
            print("Cuenta bloqueada.")
