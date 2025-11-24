numero_empleados = int(input("Escriba el número de empleados en el almacén: "))
mayor_salario = 0
empleado_con_mayor_salario = ""

for i in range(numero_empleados):
    nombre = input("Ingrese el nombre del empleado: ")
    salario = int(input("Ingrese el salario del empleado: "))
    
    if salario > mayor_salario:
        mayor_salario = salario
        empleado_con_mayor_salario = nombre

print(f"El empleado con el mayor salario en el almacén es {empleado_con_mayor_salario} con un salario de {mayor_salario}")
