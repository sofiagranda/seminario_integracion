desempeno = int(input("Ingrese el desempeño del empleado del almacén entre 1 y 5: "))
salario = int(input("Ingrese el salario del empleado en el almacén: "))

if desempeno == 1:
    bonus = salario * 0.02
elif desempeno == 2:
    bonus = salario * 0.05
elif desempeno == 3:
    bonus = salario * 0.10
elif desempeno == 4:
    bonus = salario * 0.15
else:
    bonus = 0

total = salario + bonus

print(f"El salario total del empleado en el almacén, incluyendo el bonus, es: {total}")
