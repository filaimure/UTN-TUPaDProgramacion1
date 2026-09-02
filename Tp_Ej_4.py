# TP INTEGRADOR "REPETITIVAS" EJ: 4
# ALUMNO: JANO MONTEROS
# DNI: 45012107
# NOTA: Escribo las variables en ingles porque me gusta como queda :)
# PSDT: Le puse emmojis para que quede mas estetico y use import time, para dar sensacion de carga
# saque los emojis de aca https://emojiterra.com/es/search/DORMIR/
#---------------------------------------------------------------------------------------------------------------#
# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
# limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
#     • energia = 100
#     • tiempo = 12
#     • cerraduras_abiertas = 0
#     • alarma = False
#     • codigo_parcial = ""
# Validaciones obligatorias
#     • No usar try/except.
#     • Pedir nombre del agente y validar con .isalpha() en un while.
#     • Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
#     • El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas 
# (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.).
# Regla anti-spam (muy importante) Para evitar que el jugador gane  eligiendo 
# “Forzar cerradura” 3 veces seguidas al iniciar:
# ✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#     • se cobra el costo normal (-20 energía, -2 tiempo)
#     • NO abre cerradura, y se activa la alarma automáticamente (alarma = True) 
#       porque “la cerradura se trabó”.
#     • Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
#     • Menú de acciones (se repite mientras el juego siga)
#     • El juego continúa mientras:
#     • energia > 0, tiempo > 0, cerraduras_abiertas < 3
#     • y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú:
#---------------------------------------------------------------------------------------------------------------#
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#     • Si la energía está por debajo de 40, hay “riesgo de alarma”:
#     • pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#     • Si no hay alarma, abre 1 cerradura.
#     • Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.
#---------------------------------------------------------------------------------------------------------------#
# 2. Hackear panel (costo: -10 energía, -3 tiempo)
#     • Debe usar un for de 4 pasos mostrando progreso.
#     • En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
#     • Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan
#---------------------------------------------------------------------------------------------------------------#
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
# Regla de bloqueo por alarma:
#     • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema
#       se bloquea y se pierde.
# Condiciones de fin
#     • Si cerraduras_abiertas == 3 → VICTORIA
#     • Si energia <= 0 o tiempo <= 0 → DERROTA
#     • Si se bloquea por alarma → DERROTA (bloqueo)
#---------------------------------------------------------------------------------------------------------------#
import time
energy = 100
clock = 12
alarm = False
partial_code = ""
opened_locks = 0
lock_try = 0
resting = ""
#---------------------------------------------------------------------------------------------------------------#
print("• Eres un agente que intenta abrir una bóveda con 3 cerraduras. ")
time.sleep(1.2)
print("• Tenés energía y tiempo limitados: 12 minutos y 100 de energia maxima.")
time.sleep(1.2)
print("• Si abres las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.")
time.sleep(1.2)
print("• Puedes descansar, lo que recuperara +15 de tu energia.")
time.sleep(1.2)
print("• Descansar te costara -1 minuto de tiempo total")
time.sleep(1.2)
agent = input("Cual es su nombre agente?: ")
while not agent.replace(" ", "").isalpha():
    print("Su nombre solo debe contener letras.")
    agent = input("Ingrese su nombre correctamente: ").strip()
    agent = input("Cual es su nombre agente?: ")
#---------------------------------------------------------------------------------------------------------------#
print("-----------------------------------------------------------")
print("Bienvenido agente:",agent)
print("Te ecuentras frente a una de las cerraduras de la boveda 💲")
print("Energia actual:",energy)
print("Tiempo restante:",clock)
print("Cerraduras abiertas:",opened_locks)
print("Tienes 3 opciones:")
print("1. Forzar cerradura ➞ 🔓")
print("2. Hackear panel ➞ 👨‍💻")
print("3. Descansar ➞ 🛌 ")
print("-----------------------------------------------------------")
agent_desition = input("Que decicion tomaras?(1-2-3): ")
while not agent_desition.isdigit():
    print("Solo tienes permitido ingresar valores numericos")
    agent_desition = input("Opcion numero?(1-2-3): ")
while int(agent_desition) < 1 or int(agent_desition) > 3:
        print("Esa opcion no esta disponible")
        agent_desition = input("Opcion numero?(1-2-3): ")
#---------------------------------------------------------------------------------------------------------------#
while (alarm != True) and (clock > 0) and (energy > 0) and opened_locks < 3 and lock_try < 3:
    if int(agent_desition) == 1:
          print("------------------------------------------------------------")
          print("Forzar la cerradura te costara -20 de energia y -2 de tiempo")
          print("Tu estado actual es:")
          print("Energia:",energy)
          print("Tiempo:",clock)
          print("------------------------------------------------------------")
          the_deal = input("Deseas continuar?Si/No:").lower()
          while not the_deal.isalpha():
              print("Solo tienes permitido ingresar letras")
              the_deal = input("Deseas continuar?Si/No:").lower()
          while the_deal != "si" and the_deal != "no":
              print("Solo tienes permitido ingresar (si) o (no)")
              the_deal = input("Deseas continuar?Si/No:").lower()
#---------------------------------------------------------------------------------------------------------------#
          if the_deal == "si":
               lock_try += 1
               energy -= 20
               clock -= 2
#---------------------------------------------------------------------------------------------------------------#  
               if lock_try == 3:
                    alarm = True
#---------------------------------------------------------------------------------------------------------------#  
               print("-------------ATENCION----------------")
               print("Puedes ingresar el 1, el 2 y el 3")
               print("Uno de ellos haran sonar la alarma 🔔")
               print("-------------------------------------")
               the_code = input("Que numero ingresaras?: ")
               while not the_code.isdigit():
                    print("Solo tienes permitido ingresar valores numericos")
                    the_code = input("Que numero ingresaras?: ")
#---------------------------------------------------------------------------------------------------------------#
               if int(the_code) == 3:
                print("Forzando cerradura...")
                time.sleep(1.2)
                print("Removiendo resortes...")
                time.sleep(1.2)
                print("Desarmando mecanismo...")
                time.sleep(1.2)
                print("Desarticulando engranajes...")
                time.sleep(1.2) 
                print("--------------------------------------")
                print("APERTURA FALLIDA, ALARMA ACTIVADA 💀!")
                print("Has perdido.")
                print("--------------------------------------")
                alarm = True
#---------------------------------------------------------------------------------------------------------------#
               elif int(the_code) == 2 or int(the_code) == 1:
                   opened_locks += 1
                   print("Forzando cerradura...")
                   time.sleep(1.2)
                   print("Removiendo resortes...")
                   time.sleep(1.2)
                   print("Desarmando mecanismo...")
                   time.sleep(1.2)
                   print("Desarticulando engranajes...")
                   time.sleep(1.2)          
                   print("--------------------------------------")       
                   print("HAS CONSEGUIDO ABRIR UNA CERRADURA!")
                   print("--------------------------------------")
#---------------------------------------------------------------------------------------------------------------#
          elif the_deal == "no":
              print("----------------------")
              print("Has decidido no actuar")
              print("----------------------")
              pass
#---------------------------------------------------------------------------------------------------------------#
    elif int(agent_desition) == 2:
        lock_try = 0
        print("---------------------------------------------------------------")
        print("Hackear la computadora te costara -10 de energia y -3 de tiempo")
        print("Tu estado actual es:")
        print("Energia:",energy)
        print("Tiempo:",clock)
        print("---------------------------------------------------------------")
        the_deal = input("Deseas continuar?Si/No:").lower()
        while the_deal != "si" and the_deal != "no":
            print("Solo tienes permitido ingresar si o no")
            the_deal = input("Deseas continuar?Si/No:").lower()
#---------------------------------------------------------------------------------------------------------------#  
        if the_deal == "si":
            energy -= 10
            clock -= 3
            for Hacking in range(4):
                partial_code += "A"
                print("Hackeando:",partial_code,end=" ",flush=True)
                time.sleep(1.2)
            print("\n----------------------------------------------")
            print("Hackeo completado, Resultado final:",partial_code)
            print("------------------------------------------------")
#---------------------------------------------------------------------------------------------------------------#  
            if len(partial_code) >= 8:
                opened_locks += 1
                partial_code = ""
                print("--------------------------------------")
                print("HAS ABIERTO UNA CERRADURA EXITOSAMENTE!")
                print("--------------------------------------")
#---------------------------------------------------------------------------------------------------------------#  
        elif the_deal == "no":
            print("----------------------")
            print("Has decidido no actuar")
            print("----------------------")
            pass
#---------------------------------------------------------------------------------------------------------------#
    elif int(agent_desition) == 3:
        lock_try = 0
        print("------------------------------------------------------------------")
        print("Descansar te recobrara +15 de energia pero te cobrara -1 de tiempo")
        print("Tu estado actual es:")
        print("Energia:",energy)
        print("Tiempo:",clock)
        print("------------------------------------------------------------------")
        the_deal = input("Deseas continuar?Si/No:").lower()
        while the_deal != "si" and the_deal != "no":
            print("Solo tienes permitido ingresar si o no")
            the_deal = input("Deseas continuar?Si/No:").lower()
#---------------------------------------------------------------------------------------------------------------#  
        if the_deal == "si":
            energy += 15
            if energy > 100:
                energy = 100
                clock += 1
                print("----------------------------------------------------------")
                print("No puedes descansar ya tienes suficiente energia completa.")
                print("----------------------------------------------------------")
                pass
#---------------------------------------------------------------------------------------------------------------#  
            else:
                print("Descansando:",end="")
                for Hacking in range(4):
                    resting += "...Z "
                    print(resting,end="",flush=True)
                    time.sleep(1.2)
                print("\n----------------------------------")
                print("Has recuperado 15 puntos de energia!")
                print("------------------------------------")
#---------------------------------------------------------------------------------------------------------------#  
        elif the_deal == "no":
            print("----------------------")
            print("Has decidido no actuar")
            print("----------------------")
            pass
#---------------------------------------------------------------------------------------------------------------#            
    print("----------------------------------------------------------")
    print("Te ecuentras frente a una de las cerraduras de la boveda 💲")
    print("Energia actual:",energy)
    print("Tiempo restante:",clock)
    print("Cerraduras abiertas:",opened_locks)
    print("Tienes 3 opciones:")
    print("1. Forzar cerradura ➞ 🔓")
    print("2. Hackear panel ➞ 👨‍💻")
    print("3. Descansar ➞ 🛌 ")
    print("---------------------------------------------------------")
    agent_desition = input("Que decicion tomaras?(1-2-3): ")
    while not agent_desition.isdigit():
        print("Solo tienes permitido ingresar valores numericos")
        agent_desition = input("Opcion numero?(1-2-3): ")
    while int(agent_desition) < 1 or int(agent_desition) > 3:
        print("Esa opcion no esta disponible")
        agent_desition = input("Opcion numero?(1-2-3): ")
#---------------------------------------------------------------------------------------------------------------#            
if opened_locks == 3 and lock_try < 3:
    print("---------------------------------------------------------")
    print("Lo has conseguido! abriste las 3 cerraduras con exito 🥳!")
    print("MISION CUMPLIDA! 👏 👏 👏") 
    print("---------------------------------------------------------")
elif energy <= 0:
    print("-------------------------------------")
    print("Te has quedado sin energia! 😴 😴 😴")
    print("MISION FALLIDA 💀")
    print("-------------------------------------")
elif clock <= 0:
    print("-------------------------------------")
    print("Se te a acabado el tiempo!")
    print("MISION FALLIDA 💀")
    print("-------------------------------------")
elif lock_try == 3:
    print("-------------------------------------")
    print("FORZASTE LAS CERRADURAS DEMASIADO SEGUIDO!")
    print("SISTEMA BLOQUEADO 🚨")
    print("MISION FALLIDA 💀")
    print("-------------------------------------")
elif alarm:
    print("-------------------------------------")
    print("ALARMA ACTIVADA ¡🔔! ¡🔔! ¡🔔!")
    print("SISTEMA BLOQUEADO 🚨")
    print("MISION FALLIDA 💀")
    print("-------------------------------------")
#---------------------------------------------------------------------------------------------------------------#  
       
