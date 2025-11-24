antiguedad = int(input("Ingrese los años de antigüedad en el almacén: "))

if antiguedad < 1:
    vacaciones = 0
elif antiguedad < 3:
    vacaciones = 3
elif antiguedad < 5:
    vacaciones = 10
else:
    vacaciones = 15

print(f"El empleado tiene {vacaciones} días de vacaciones por antigüedad en el almacén.")
