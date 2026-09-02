# TP INTEGRADOR "REPETITIVAS" EJ: 5
# ALUMNO: JANO MONTEROS
# DNI: 45012107
# NOTA: Escribo las variables en ingles porque me gusta como queda :)
#---------------------------------------------------------------------------------------------------------------#
# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
# 1. Descripción del Escenario.
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un
# usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
# objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.
# Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de
# control (if/elif/else), ciclos (while y for) y validación de datos estricta.
#---------------------------------------------------------------------------------------------------------------#
# 2. Requerimientos Técnicos.
#    A. Tipos de Datos
#    Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
#      • String: Para el nombre del jugador.
#      • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
#      • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).
#      • Boolean: Para controlar si el juego sigue activo o quién tiene el turno. 
#    B. Reglas de Validación (¡Importante!)
#      • No está permitido usar bloques try / except.
#      • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
#      • Para validar números, debes usar el método .isdigit() dentro de un ciclo while.
#---------------------------------------------------------------------------------------------------------------#
# 3. Flujo del Programa.
#    Paso 1: Configuración del Personaje
#    El programa inicia pidiendo el nombre del Gladiador.
#    • Validación: El nombre solo puede contener letras. Si el usuario ingresa números,
#      símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" 
#      y volver a preguntar hasta que sea válido.
#     (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------#
#    Paso 2: Inicialización de Estadísticas 
#    El programa debe definir las variables iniciales (sin preguntar al usuario):
#    • Vida del Gladiador: 100 (int)
#    • Vida del Enemigo: 100 (int)
#    • Pociones de Vida: 3 (int)
#    • Daño base "Ataque Pesado": 15 (int)
#    • Daño base del enemigo: 12 (int)
#    • Turno Gladiador : True (booleano)
#    (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------# 
#    Paso 3: El Ciclo de Combate
#    El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0
#    puntos de vida.
#    (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------# 
#    Paso 3: El Ciclo de Combate
#    Turno del Jugador:
#    Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3
#    opciones:
#         1. Ataque Pesado
#         2. Ráfaga Veloz (Requiere uso de for)
#         3. Curar
#---------------------------------------------------------------------------------------------------------------# 
#    • Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo
#      ingresado sea un número (.isdigit()).
#      2. Verificar que el número sea 1, 2 o 3.
#    • Si falla alguna validación, mostrar mensaje de error y volver a pedir. 
#    (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------# 
#     Lógica de las Acciones:
#     Acción A: Ataque Pesado (Opción 1)
#     • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador
#       realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
#     • Resta el daño a la vida del enemigo.
#     • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
#     (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------# 
#     Acción B: Ráfaga Veloz (Opción 2)
#     • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
#     • El bucle debe repetirse 3 veces (usando range).
#     • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.
#       2. Muestra el mensaje: " > Golpe conectado por 5 de daño".
#          Acción C: Curar (Opción 3) 
#          • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
#          • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el
#            enemigo ataca igual).
#     (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------# 
#     • Turno del Enemigo:
#       Justo después de tu acción, el enemigo ataca automáticamente.
#     • Resta el daño base del enemigo (12) a tu vida.
#     • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
#     Paso 4: Fin del Juego
#       Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
#     • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
#     • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate." 
#     (COMPLETADO)
#---------------------------------------------------------------------------------------------------------------#
import time
main_health = 100 
enemy_health = 100 
life_potions = 3 
base_damage = 15 #daño pesado
basic_enemy_damage = 12 
gladiator_turn = True #booleano
critic_damage = 0.0
#---------------------------------------------------------------------------------------------------------------#
gladiator = input("Dime tu nombre GLADIADOR: ")
while not gladiator.replace(" ", "").isalpha():
    print("Tu nombre solo debe contener letras.")
    gladiator = input("Dime tu nombre GLADIADOR: ")
print("#-------------------------------------------------------#")
print(f"Bienvenido a la arena de combate gladiador {gladiator}!")
print(f"El adversario frente a ti tiene {enemy_health} puntos de vida")
print(f"Tu tienes {main_health} puntos de vida")
print("Cual sera tu primer movimiento???")
print("1. Ataque Pesado")
print("2. Ráfaga Veloz")
print("3. Curar")
print("#-------------------------------------------------------#")
move = input("Toma tu descicion guerrero (1, 2 o 3): ")
#---------------------------------------------------------------------------------------------------------------# 
while not move.isdigit() or int(move) not in (1, 2, 3):
    print("Solo puedes ingresar el 1 el 2 y el 3!")
    move = input("Toma tu descicion guerrero (1, 2 o 3): ")
#---------------------------------------------------------------------------------------------------------------# 
while int(main_health) > 0 and int(enemy_health) > 0:
#---------------------------------------------------------------------------------------------------------------# 
    if int(move) == 1:
        if int(enemy_health) < 20:
            critic_damage = (float(base_damage) * 1.5)
            enemy_health -= critic_damage
            main_health -= basic_enemy_damage
            print("Tu enemigo se tambalea por las heridas del combate...")
            time.sleep(1.2)
            print("Tu alzas tu arma de combate y arremetes con una fuerza inaudita...")
            time.sleep(1.2)
            print(f"¡Has acertado a tu enemigo un impacto critico!")
            time.sleep(1.2)
            print(f"Ocacionaste {critic_damage} puntos de daño!")
            time.sleep(1.2)
            print("Tu enemigo recibe un gran daño...")
            time.sleep(1.2)
            print("Pero con sus ultimas fuerzas te propina un golpe!")
            time.sleep(1.2)
            print("EL golpe ocasiona que pierdas (12) puntos de vida.")
#---------------------------------------------------------------------------------------------------------------# 
        else:
            enemy_health -= base_damage
            main_health -= basic_enemy_damage
            print("#-------------------------------------------------------#")
            print("Has decidido atacar a tu oponente!")
            time.sleep(1.2)
            print("Te acercas y con un golpé sertero dañas a tu enemigo...")
            time.sleep(1.2)
            print(f"Tu ataque a ocacionado ({base_damage}) puntos de daño!")
            time.sleep(1.2)
            print("Tu enemigo se recompone y regresa con un contragolpe!")
            time.sleep(1.2)
            print(f"Has perdido ({basic_enemy_damage}) puntos de vida.")
#---------------------------------------------------------------------------------------------------------------# 
    elif int(move) == 2:
        main_health -= basic_enemy_damage
        print("#-------------------------------------------------------#")
        for speed_attack in range(3):
            enemy_health -= 5
            print("Golpe conectado! Has inflingido (5) puntos de daño!")
            time.sleep(1.2)
        print("Tu Ráfaga Veloz a ocasionado 15 puntos de daño total!!!")
        time.sleep(1.2)
        print("Tu enemigo se recupera del masivo ataque y devuelve un golpe...")
        time.sleep(1.2)
        print(f"Has sufrido un ataque y pierdes (12) puntos de vida!")
#---------------------------------------------------------------------------------------------------------------# 
    elif int(move) == 3:
        if int(life_potions) > 0:
            main_health += 30
            if int(main_health) > 100:
                main_health = 100
                main_health -= basic_enemy_damage
                print("#-------------------------------------------------------#")
                print("Revisas tu bolsa en busqueda de posciones curativas...")
                time.sleep(1.2)
                print("Pero recuerdas que... YA TIENES SUFICIENTES PUNTOS DE VIDA!!!")
                time.sleep(1.2)
                print("Tu enemigo aprovecha tu mala gestion y ataca!")
                time.sleep(1.2)
                print("Has sido atacado suciamente... pierdes (12) puntos de vida.")
            else:
                life_potions -= 1
                main_health -= basic_enemy_damage
                print("#-------------------------------------------------------#")
                print("Revisas tu bolsa en busqueda de posciones curativas...")
                time.sleep(1.2)
                print("Has encontrado una poscion!")
                time.sleep(1.2)
                print("LA CONSUMES Y RECUPERAS (30) PUNTOS DE VIDA!")
                time.sleep(1.2)
                print("Tu enemigo aprovecha tu recuperacion y...")
                time.sleep(1.2)
                print("ACIERTA UN GOLPE!!!")
                time.sleep(1.2)
                print("Has conseguido (30) puntos de vida pero pierdes (12).")
#---------------------------------------------------------------------------------------------------------------# 
        elif int(life_potions) == 0:
            main_health -= basic_enemy_damage
            print("#-------------------------------------------------------#")
            print("Revisas tu bolsa en busqueda de posciones curativas...")
            time.sleep(1.2)
            print("¡OH NO! ya no te quedan pociones!")
            time.sleep(1.2)
            print("Tu enemigo aprovecha tu desconcentracion y...")
            time.sleep(1.2)
            print("ATACA!!!")
            time.sleep(1.2)
            print("Has sufrido un ataque, pierdes (12) puntos de vida.")
#---------------------------------------------------------------------------------------------------------------#
    print("#-----------------------------------#")
    print(f"Sigamos con el combate {gladiator}!")
    print(f"Tu adversario tiene {enemy_health} puntos de vida")
    print(f"A ti te quedan {main_health} puntos de vida")
    print("Cual sera tu proximo movimiento???")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    print("#-----------------------------------#")
    move = input("Que es lo que haras?(1, 2 o 3): ")
#---------------------------------------------------------------------------------------------------------------# 
    while not move.isdigit() or int(move) not in (1, 2, 3):
        print("Solo puedes ingresar el 1 el 2 y el 3!")
        move = input("Toma tu descicion guerrero (1, 2 o 3): ")
#---------------------------------------------------------------------------------------------------------------# 
if main_health <= 0 and enemy_health > 0:
    print("#-------------------------------------------------------#")
    print("DERROTA. Has caído en combate!!!")
    print("#-------------------------------------------------------#")
elif enemy_health <= 0 and main_health > 0:
    print("#-------------------------------------------------------#")
    print(f"¡VICTORIA! {gladiator} ha ganado la batalla!!!")
    print("#-------------------------------------------------------#")
elif enemy_health <= 0 and main_health <= 0:
    print("#-------------------------------------------------------#")
    print("DERROTA. Ambos han muerto en combate!!!.")
    print("#-------------------------------------------------------#")
#---------------------------------------------------------------------------------------------------------------# 
