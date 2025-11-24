dias = int(input("¿Cuántos días vas a cargar para el registro de asistencia en el almacén? "))
tardes = 0

for i in range(dias):
    marca = input(f"Día {i + 1} (T = tarde, O = ok, P = permiso): ").strip().upper()
    if marca == "T":
        tardes += 1

print(f"Tardanzas totales del empleado en el almacén: {tardes}")
