# Ejercicio 4  — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
# energia = 100
# tiempo = 12
# cerraduras_abiertas = 0
# alarma = False
# codigo_parcial = ""
# Validaciones obligatorias
# No usar try/except.
# Pedir nombre del agente y validar con .isalpha() en un while.
# Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
# El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.).
# Regla anti-spam (muy importante)
# Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar:
# ✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
# se cobra el costo normal (-20 energía, -2 tiempo),
# NO abre cerradura, y
# se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”.
# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
# Menú de acciones (se repite mientras el juego siga) El juego continúa mientras:
# energia > 0, tiempo > 0, cerraduras_abiertas < 3
# y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
# Forzar cerradura (costo: -20 energía, -2 tiempo) o 	Si la energía está por debajo de 40, hay “riesgo de alarma”:
# 	▪ 	pedir un número 1-3 (validado). Si elige 3 → alarma=True.
# Si no hay alarma, abre 1 cerradura.
# Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.
# Hackear panel (costo: -10 energía, -3 tiempo) o 	Debe usar un for de 4 pasos mostrando progreso. o 	En cada paso sumar una letra al codigo_parcial (por ejemplo “A”). o 	Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan.
# Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
# Regla de bloqueo por alarma
# • 	Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
# Condiciones de fin
# Si cerraduras_abiertas == 3 → VICTORIA • 	Si energia <= 0 o tiempo <= 0 → DERROTA
# Si se bloquea por alarma → DERROTA (bloqueo)

# Creación del juego de escape room: La Bóveda
# Variables iniciales
import random

energia: int = 100
tiempo: int = 12
cerraduras_abiertas: int = 0
alarma: bool = False
codigo_parcial: str = ""
intentos_forzar_seguidos: int = 0
numero_aleatorio: int = 0

# Entrada del agente (Requerimiento 1 enunciado)

nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.isalpha():
    print("Error: el nombre del agente debe contener solo letras.")
    nombre_agente = input("Ingrese el nombre del agente: ")
print(
    f"Bienvenido, Agente {nombre_agente.capitalize()}. ¡Comencemos la misión para abrir la bóveda!"
)

# Función para mostrar el estado actual del juego


def mostrar_estado() -> None:
    """Imprime el estado actual del juego, incluyendo energía, tiempo, cerraduras abiertas, estado de la alarma y código parcial si existe."""
    print(f"\nEstado actual:")
    print(f"Energía: {energia}")
    print(f"Tiempo restante: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma activada: {'Sí' if alarma else 'No'}")
    if codigo_parcial:
        print(f"Código parcial obtenido: {codigo_parcial}")


# Función para mostrar el menú de acciones


def mostrar_menu() -> None:
    """Muestra el menú de acciones para el juego."""
    print("\nMenú de acciones:")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")


# Función para forzar una cerradura


def forzar_cerradura() -> None:
    """Intenta forzar una cerradura, aplicando las reglas de energía, tiempo y riesgo de alarma."""
    global energia, tiempo, cerraduras_abiertas, alarma, intentos_forzar_seguidos, random, numero_aleatorio
    energia -= 20
    tiempo -= 2
    intentos_forzar_seguidos += 1
    print("Intentando forzar la cerradura...")
    if energia < 40 and not alarma and intentos_forzar_seguidos >= 3:
        print("¡Riesgo de alarma! Elige un número del 1 al 3:")
        opcion_alarma = input("Número: ")
        while (
            not opcion_alarma.isdigit()
            or int(opcion_alarma) < 1
            or int(opcion_alarma) > 3
        ):
            print("Error: ingrese un número válido entre 1 y 3.")
            opcion_alarma = input("Número: ")
        numero_aleatorio = random.randint(1, 3)
        if int(opcion_alarma) == numero_aleatorio:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
            return
    if intentos_forzar_seguidos == 3:
        alarma = True
        print("¡La cerradura se trabó por forzar seguidas! Alarma activada.")
        return
    if not alarma:
        cerraduras_abiertas += 1
        print("¡Cerradura abierta exitosamente!")


# Función para hackear el panel


def hackear_panel() -> None:
    """Intenta hackear el panel, aplicando las reglas de energía, tiempo y progreso del código parcial."""
    global energia, tiempo, cerraduras_abiertas, codigo_parcial, random, intentos_forzar_seguidos
    intentos_forzar_seguidos = 0
    energia -= 10
    tiempo -= 3
    print("Hackeando el panel...")
    for paso in range(1, 5):
        codigo_parcial += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print(f"Progreso del hackeo: Paso {paso}/4 - Código parcial: {codigo_parcial}")
    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
        cerraduras_abiertas += 1
        print("¡Cerradura abierta automáticamente por hackeo exitoso!")


# Función para descansar


def descansar() -> None:
    """Permite al agente descansar, recuperando energía pero perdiendo tiempo, y aplicando penalización extra si la alarma está activada."""
    global energia, tiempo, alarma, intentos_forzar_seguidos
    intentos_forzar_seguidos = 0
    energia += 15
    if energia > 100:
        energia = 100
    tiempo -= 1
    if alarma:
        energia -= 10
        print("Descansando... pero la alarma está activada, pierdes energía extra.")
    else:
        print("Descansando... energía recuperada.")


# Bucle principal del juego
while True:
    mostrar_estado()
    if cerraduras_abiertas == 3:
        print("¡Felicidades, has abierto la bóveda! VICTORIA")
        break
    if energia <= 0 or tiempo <= 0:
        print("Has quedado sin energía o sin tiempo. DERROTA")
        break
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("La alarma ha bloqueado el sistema. DERROTA (bloqueo)")
        break
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese un número válido entre 1 y 3.")
        opcion = input("Seleccione una opción: ")
    opcion = int(opcion)
    if opcion == 1:
        forzar_cerradura()
    elif opcion == 2:
        hackear_panel()
    elif opcion == 3:
        descansar()
