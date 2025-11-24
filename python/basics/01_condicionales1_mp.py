nombre_producto = input("Nombre del producto: ")
stock = int(input("Unidades en stock: "))
precio = float(input("Precio del producto: "))
categoria_especial = input("¿Está registrado bajo una categoría especial? (s/n): ").lower() == "s"

if stock >= 20 and (precio > 100 or categoria_especial):
    print(f"El producto '{nombre_producto}' es elegible para ser añadido al inventario.")
else:
    print(f"El producto '{nombre_producto}' no es elegible para ser añadido al inventario.")
