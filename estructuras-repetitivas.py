# 1. Mostrar del 1 hasta el número ingresado (bucle while)

n = int(input("Ingresa un número entero positivo: "))
i = 1
while i <= n:
    print(i)
    i += 1



# 2. Números pares entre 1 y 20 (bucle for)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)



#3. Contar los dígitos de un número (bucle while)

n = int(input("Ingresa un número entero positivo: "))
contador = 0
while n > 0:
    n //= 10
    contador += 1
print("Cantidad:", contador)



#4. Suma de los números del 1 al 100 (bucle for)

suma = 0
for i in range(1, 101):
    suma += i
print("la suma es:", suma)



#5. Contar desde un número hasta 0 en reversa (bucle while)

n = int(input("ingresa un numero entero: "))
while n >= 0:
    print(n)
    n -= 1


#6. Tabla de multiplicar (bucle for)

n = int(input("ingresa un numero para mostrar su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


#7. Números impares hasta un número (bucle while)

n = int(input("Ingresa un número entero positivo: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1


#8. Serie de Fibonacci hasta el término n (bucle for)

n = int(input("¿Cuántos términos de Fibonacci deseas?: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b


#9. Factorial de un número (bucle while)

n = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("El factorial es:", factorial)


#10. Verificación de contraseña (simulando do-while con while)

contraseña_correcta = ""
while True:
    intento = input("Ingresa la contraseña: ")
    if intento == contraseña_correcta:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")




