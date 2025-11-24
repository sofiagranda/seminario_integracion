horast = int(input("Ingresa el total de horas trabajadas en el almacén esta semana: "))
pagoh = int(input("Ingresa el pago por hora del empleado en el almacén: "))

if horast > 40:
    horas_normales = 40 * pagoh
    horas_extras = (horast - 40) * (pagoh * 1.5)
    total_semanal = horas_normales + horas_extras
else:
    total_semanal = horast * pagoh

print(f"El pago semanal del empleado por las horas trabajadas en el almacén es: {total_semanal}")
