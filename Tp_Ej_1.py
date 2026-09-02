#---------------------------------------------------------------------------------------------------------------#
# TP INTEGRADOR "REPETITIVAS" EJ: 1
# ALUMNO: JANO MONTEROS
# DNI: 45012107
# NOTA: Escribo las variables en ingles porque me gusta como queda :)
#---------------------------------------------------------------------------------------------------------------#
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
#---------------------------------------------------------------------------------------------------------------#
discount = 0
non_discount = 0 
user_name = input("Ingrese su nombre: ").strip()
while not user_name.isalpha() or user_name == "":
    if not user_name.isalpha():
        print("Solo tiene permitido ingresar letras.")
    elif user_name == "":
        print("Usted no ingreso nada")
    user_name = input("Ingrese su nombre: ").strip()
#---------------------------------------------------------------------------------------------------------------#
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).    
#---------------------------------------------------------------------------------------------------------------#
product_amount = input("Ingrese la cantidad de productos a adquirir: ")
while (not product_amount.isdigit()) or ((int(product_amount)) <= 0):
    if not product_amount.isdigit():
        print("Debe ingresar un numero, cualquier otro tipo de valor sera rechazado.")
    elif int(product_amount) == 0:
        print("El 0 no es un numero valido o admisible")
    elif int(product_amount) < 0:
        print("No puede ingresar numeros negativos")
    product_amount = input("Ingrese la cantidad de productos a adquirir: ")
#---------------------------------------------------------------------------------------------------------------#
# 3. Por cada producto (usar for):
#                                a. Pedir precio (entero, validar .isdigit()).
#                                b. Pedir si tiene descuento S/N (validar con while, aceptar s o n en
#                                  cualquier mayuscula/minuscula).
#                                c. Si tiene descuento: aplicar 10% al precio de ese producto.
#---------------------------------------------------------------------------------------------------------------#
for rounds in range(1,int(product_amount)+1):
    product_price = input(f"Cual es el precio del producto numero {rounds}?: ")
    while not product_price.isdigit() or int(product_price) <= 0:
        print("Precio inválido")
        product_price = input(f"Cual es el precio del producto numero {rounds}?: ")
    product_price = int(product_price)
    validation = input("Este producto tiene descuento?(S/N): ").lower()
    while validation != "s" and validation != "n":
        print("Solo tiene perimitido ingresar S o N")
        validation = input("Este producto tiene descuento?(S/N): ").lower()
    non_discount += int(product_price)
    if validation == "s":
        discount += int(product_price) * 0.9
    else:
        discount += int(product_price)
#---------------------------------------------------------------------------------------------------------------#
# 4. Al final mostrar:
#                    a. Total sin descuentos
#                    b. Total con descuentos
#                    c. Ahorro total
#                    d. Promedio por producto (usar float y formatear con :.2f, ejem:
#                       • x = 3.14159
#                       • print(f"{x:.2f}"))
#---------------------------------------------------------------------------------------------------------------#
saving = non_discount - discount
average = float(discount) / float(product_amount)
print("Cantidad de productos:",product_amount)
print(f"Total sin descuentos: ${non_discount:.2f}")
print(f"Total con descuentos: ${discount:.2f}")
print(f"Ahorro: ${saving:.2f}")
print(f"Promedio por producto: {average:.2f}")