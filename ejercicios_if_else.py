# Ejercicio 1: Número positivo, negativo o cero
num = int(input("Ingresa un número: "))
if num > 0:
    print("Es positivo")
elif num < 0:
    print("Es negativo")
else:
    print("Es cero")


# Ejercicio 2: Número par o impar
num = int(input("Ingresa un número entero: "))
if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")


# Ejercicio 3: Mayor de edad
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Ejercicio 4: Múltiplo de 5
num = int(input("Ingresa un número: "))
if num % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 5")


# Ejercicio 5: Descuento por edad
edad = int(input("Ingresa tu edad: "))
if edad >= 60:
    print("Aplica para descuento del 50%")
else:
    print("No aplica para descuento")


# Ejercicio 6: Calificación aprobatoria
nota = int(input("Ingresa la calificación (0-100): "))
if nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")


# Ejercicio 7: Día de la semana
num = int(input("Ingresa un número del 1 al 7: "))
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
if 1 <= num <= 7:
    print("Día:", dias[num - 1])
else:
    print("Número inválido")


# Ejercicio 8: Número mayor entre dos
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if a > b:
    print("El mayor es:", a)
elif b > a:
    print("El mayor es:", b)
else:
    print("Son iguales")


# Ejercicio 9: Mayor entre tres números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
mayor = max(a, b, c)
print("El mayor es:", mayor)


# Ejercicio 10: Clasificación de ángulos
angulo = int(input("Ingresa el valor del ángulo en grados: "))
if angulo < 90:
    print("Ángulo agudo")
elif angulo == 90:
    print("Ángulo recto")
elif angulo < 180:
    print("Ángulo obtuso")
elif angulo == 180:
    print("Ángulo llano")
else:
    print("Ángulo inválido")


# Ejercicio 11: Cálculo de impuestos
salario = float(input("Ingresa tu salario mensual: "))
if salario < 10000:
    print("Impuesto: 0%")
elif salario <= 30000:
    print("Impuesto: 10%")
else:
    print("Impuesto: 20%")


# Ejercicio 12: Clasificación de números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
if a == 0 or b == 0 or c == 0:
    print("Hay ceros")
elif a > 0 and b > 0 and c > 0:
    print("Todos positivos")
elif a < 0 and b < 0 and c < 0:
    print("Todos negativos")
else:
    print("Mixtos")


# Ejercicio 13: Verificación de año bisiesto
año = int(input("Ingresa un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")


# Ejercicio 14: Conversión de calificaciones
nota = int(input("Ingresa la calificación (0-100): "))
if 90 <= nota <= 100:
    print("A")
elif 80 <= nota <= 89:
    print("B")
elif 70 <= nota <= 79:
    print("C")
elif 60 <= nota <= 69:
    print("D")
else:
    print("F")


# Ejercicio 15: Comparación de tres longitudes
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))
if a + b > c and a + c > b and b + c > a:
    print("Pueden formar un triángulo")
else:
    print("No pueden formar un triángulo")


# Ejercicio 16: Calculadora de descuentos
precio = float(input("Ingresa el precio del producto: "))
if precio < 50:
    print("Sin descuento")
elif precio <= 100:
    print("Descuento del 5%")
else:
    print("Descuento del 10%")


# Ejercicio 17: Tipo de triángulo
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))
if a == b == c:
    print("Triángulo equilátero")
elif a == b or b == c or a == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")


# Ejercicio 18: Evaluación de temperatura
temp = float(input("Ingresa la temperatura en °C: "))
if temp < 0:
    print("Hace mucho frío")
elif temp <= 20:
    print("Clima fresco")
elif temp <= 30:
    print("Clima agradable")
else:
    print("Hace mucho calor")


# Ejercicio 19: Conversión de horas a turnos
hora = int(input("Ingresa la hora (0-23): "))
if 6 <= hora <= 11:
    print("Mañana")
elif 12 <= hora <= 17:
    print("Tarde")
elif 18 <= hora <= 23:
    print("Noche")
else:
    print("Madrugada")


# Ejercicio 20: Clasificación de IMC
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print("IMC:", round(imc, 2))
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
