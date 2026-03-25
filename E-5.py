#  Ejercicio 5  — “Escape Room:"La Arena del Gladiador"
# Descripción del Escenario
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.  Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de control (if/elif/else), ciclos (while y for) y validación de datos estricta.
# Requerimientos Técnicos
# A. Tipos de Datos
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
# • String: Para el nombre del jugador.
# • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
# • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).
# • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
# B. Reglas de Validación (¡Importante!)
# • No está permitido usar bloques try / except.
# • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.  • 	• Para validar números, debes usar el método .isdigit() dentro de un ciclo while.
# Flujo del Programa
# Paso 1: Configuración del Personaje
# El programa inicia pidiendo el nombre del Gladiador.
# • 	• Validación: El nombre solo puede contener letras. Si el usuario ingresa números, símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a preguntar hasta que sea válido.
# Paso 2: Inicialización de Estadísticas
# El programa debe definir las variables iniciales (sin preguntar al usuario):
# • Vida del Gladiador: 100 (int)
# • Vida del Enemigo: 100 (int)
# • Pociones de Vida: 3 (int)
# • Daño base "Ataque Pesado": 15 (int)
# • Daño base del enemigo: 12 (int)
# • Turno Gladiador : True (booleano)
# Paso 3: El Ciclo de Combate
# El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
# Turno del Jugador:
# Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 opciones:
# Ataque Pesado
# Ráfaga Veloz (Requiere uso de for)
# Curar
# • Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo ingresado sea un número (.isdigit()).
# 2. Verificar que el número sea 1, 2 o 3.  o Si falla alguna validación, mostrar mensaje de error y volver a pedir.
# Lógica de las Acciones:
# Acción A: Ataque Pesado (Opción 1)
# • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
# • Resta el daño a la vida del enemigo.
# • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
# Acción B: Ráfaga Veloz (Opción 2)
# • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
# • El bucle debe repetirse 3 veces (usando range).
# • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.  • 	2. Muestra el mensaje: " > Golpe conectado por 5 de daño".
# •
# Acción C: Curar (Opción 3)
# • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
# • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual).
# Turno del Enemigo:
# Justo después de tu acción, el enemigo ataca automáticamente.
# • Resta el daño base del enemigo (12) a tu vida.
# • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
# Paso 4: Fin del Juego
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
# • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
# • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."
# Ejemplo de Ejecución (Consola)
# Plaintext
# --- BIENVENIDO A LA ARENA ---
# Nombre del Gladiador: Leonidas1  Error: Solo se permiten letras.
# Nombre del Gladiador: Leonidas
# === INICIO DEL COMBATE ===
# Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3
# Elige acción:
# Ataque Pesado
# Ráfaga Veloz
# Curar
# Opción: A
# Error: Ingrese un número válido.
# Opción: 2
# >> ¡Inicias una ráfaga de golpes!
# > Golpe conectado por 5 de daño
# > Golpe conectado por 5 de daño
# > Golpe conectado por 5 de daño
# >> ¡El enemigo contraataca por 12 puntos!
# === NUEVO TURNO ===
# Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3  ...

# Creación del juego de escape room: La Arena del Gladiador

# Variables iniciales

nombre_gladadior: str = ""
vida_del_enemigo: int = 100
vida_del_gladiador: int = 100
pociones_de_vida: int = 3
Daño_Ataque_Pesado: int = 15
Daño_Base_Enemigo: int = 12
turno_gladiador: bool = True

# Entrada del gladiador

nombre_gladadior = input("Ingrese el nombre del gladiador: ")
while not nombre_gladadior.isalpha() or nombre_gladadior == "":
    print("Error: el nombre del gladiador debe contener solo letras y no estar vacío.")
    nombre_gladadior = input("Ingrese el nombre del gladiador: ")
print(
    f"Bienvenido, Gladiador {nombre_gladadior.capitalize()}. ¡Comencemos con la lucha!"
)

# Bucle principal

while True:
    if vida_del_gladiador <= 0:
        print(f"\nDERROTA. {nombre_gladadior} has caído en combate.")
        break
    if vida_del_enemigo <= 0:
        print(f"\n¡VICTORIA! {nombre_gladadior} ha ganado la batalla.")
        break
    print(
        f"\n{nombre_gladadior} (HP: {vida_del_gladiador}) vs Enemigo (HP: {vida_del_enemigo}) | Pociones: {pociones_de_vida}\n"
    )
    if not turno_gladiador:
        vida_del_gladiador -= Daño_Base_Enemigo
        print(f"\n¡El enemigo te atacó por {Daño_Base_Enemigo} puntos de daño!")
        turno_gladiador = True
    else:
        print("Elige acción:")
        print("1) Ataque Pesado")
        print("2) Ráfaga Veloz")
        print("3) Curar")
        opcion = input("Opción: ")
        while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
            print("Error: Ingrese un número válido (1, 2 o 3).")
            opcion = input("Opción: ")
        opcion = int(opcion)
        turno_gladiador: bool = (
            False  # Se asume que el jugador pierde el turno después de elegir una acción, incluso si es curar sin pociones.
        )
        if opcion == 1:
            daño_final = Daño_Ataque_Pesado
            if vida_del_enemigo < 20:
                daño_final *= 1.5
                print("¡Golpe Crítico!")
            vida_del_enemigo -= float(daño_final)
            print(f"¡Atacaste al enemigo por {float(daño_final):.2f} puntos de daño!")
        elif opcion == 2:
            print("\n¡Inicias una ráfaga de golpes!")
            for golpe in range(3):
                vida_del_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")
        elif opcion == 3:
            if pociones_de_vida > 0:
                vida_del_gladiador += 30
                if vida_del_gladiador > 100:
                    vida_del_gladiador: int = 100
                pociones_de_vida -= 1
                print("\n¡Te has curado por 30 puntos de vida!")
            else:
                print("\n¡No quedan pociones! Pierdes el turno.")
