#Variables generales
edad = input("Cual es tu edad\n")
total_dias = 90 * 365
total_semanas = 90 *52
total_meses = 90 * 12
#Variables del usario
user_dias =  total_days - (int (edad) * 365)
user_semanas = total_weeks - int (edad) * 52
user_meses = total_months - int (edad) * 12
#Datos a imprimir
print(f"te quedan {user_dias} dias, {user_dias} semanas y {user_dias} meses por vivir")
print("Considerando que vas a vivir hasta los 90")