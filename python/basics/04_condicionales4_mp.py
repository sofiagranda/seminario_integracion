salario = int(input("Ingrese el salario del empleado del almacén: "))

if salario < 1000:
    cargo = "Operativo"
elif salario <= 2000:
    cargo = "Supervisor"
else:
    cargo = "Gerente"

print(f"El cargo del empleado en el almacén es: {cargo}")
