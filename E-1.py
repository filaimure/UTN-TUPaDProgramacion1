# Ejercicio 1: "Caja del Kiosco"
# Objetivo: Simular una compra con validaciones y cálculo de total.
# Requisitos
# Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# Pedir cantidad de productos a comprar (número entero positivo, validar con
# .isdigit() en while).
# Por cada producto (usar for):
# Pedir precio (entero, validar .isdigit()).
# Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
# Si tiene descuento: aplicar 10% al precio de ese producto.
# Al final mostrar:
# Total sin descuentos o 	Total con descuentos o 	Ahorro total o 	Promedio por producto (usar float y formatear con :.2f, ejem:
#  x = 3.14159 print(f"{x:.2f}"))
# Validaciones obligatorias
# Sin try/except.
# No aceptar vacío en nombre (si queda vacío, es error).
# Cantidad > 0 (si ingresa 0, volver a pedir).
# Salida esperada (ejemplo)
# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100  Descuento (S/N): s
# Producto 2 - Precio: 50   Descuento (S/N): n
# Producto 3 - Precio: 200  Descuento (S/N): s
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.67

# Pedir nombre del cliente y validar que solo contenga letras y no esté vacío
Nombre_del_cliente = input("Ingrese el nombre del cliente: ").strip()
while not Nombre_del_cliente.isalpha():
    print("Error: El nombre debe contener solo letras y no puede estar vacío.")
    Nombre_del_cliente = input("Ingrese el nombre del cliente: ").strip()
print(f"Cliente : {Nombre_del_cliente.capitalize()}")

# Pedir cantidad de productos y validar que sea un número entero positivo
Cantidad_de_productos_str = input("Ingrese la cantidad de productos a comprar: ")
while not Cantidad_de_productos_str.isdigit() or int(Cantidad_de_productos_str) <= 0:
    print("Error: La cantidad debe ser un número entero positivo.")
    Cantidad_de_productos_str = input("Ingrese la cantidad de productos a comprar: ")
print(f"Cantidad de productos: {Cantidad_de_productos_str}")
Cantidad_de_productos_int = int(Cantidad_de_productos_str)

# Inicializar variables para el total sin descuentos, total con descuentos y precio con descuento
total_sin_descuentos = 0
total_con_descuentos = 0
precio_con_descuento = 0

# Iterar por cada producto, pedir precio y descuento, validar entradas y calcular totales
for i in range(1, Cantidad_de_productos_int + 1):
    precio_str = input(f"Precio del producto {i} : ")
    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error : el precio debe ser un numero entero positivo.")
        precio_str = input(f"Precio del producto {i} : ")
    precio_int = int(precio_str)
    total_sin_descuentos += precio_int
    descuento = input(f"Producto {i} - Precio: {precio_int}  Descuento (S/N): ").lower()
    while not descuento in ["s", "n"]:
        print("Error: Debe ingresar 'S' para sí o 'N' para no.")
        descuento = input(
            f"Producto {i} - Precio: {precio_int}  Descuento (S/N): "
        ).lower()
    if descuento == "s":
        precio_con_descuento = precio_int * 0.9
        total_con_descuentos += precio_con_descuento
    else:
        total_con_descuentos += precio_int

# Mostrar resultados
print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${total_sin_descuentos - total_con_descuentos:.2f}")
print(f"Promedio por producto: ${total_con_descuentos / Cantidad_de_productos_int:.2f}")
