numero_empleados = int(input("Ingrese el número de empleados en el almacén: "))

total_sueldo = 0

for i in range(numero_empleados):
    sueldo = int(input(f"Ingrese el sueldo del empleado {i + 1}: "))
    total_sueldo += sueldo

print(f"El total de sueldos de los empleados del almacén es: {total_sueldo}")
