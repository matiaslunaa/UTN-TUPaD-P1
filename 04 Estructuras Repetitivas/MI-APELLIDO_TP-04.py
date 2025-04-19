#Ejercicio 1
for i in range(0, 101):
    print(i)

#Ejercicio 2
numero = input("Ingresá un número entero: ")
if numero.startswith("-"):
    cantidad_digitos = len(numero) - 1
else:
    cantidad_digitos = len(numero)
print("El número tiene", cantidad_digitos, "dígitos.")

#Ejercicio 3
inicio = int(input("Ingresá el primer número: "))
fin = int(input("Ingresá el segundo número: "))
if inicio > fin:
    inicio, fin = fin, inicio
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma de los números entre", inicio, "y", fin, "es:", suma)

#Ejercicio 4
suma = 0
while True:
    numero = int(input("Ingresá un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("La suma total es:", suma)

#Ejercicio 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intento(s).")
        break
    else:
        print("Incorrecto. Probá de nuevo.")

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7
limite = int(input("Ingresá un número entero positivo: "))
if limite < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(1, limite):
        suma += i
    print("La suma de los números entre 0 y", limite, "es:", suma)

#Ejercicio 8
CANTIDAD_NUMEROS = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingresá el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\nResultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#Ejercicio 9
CANTIDAD_NUMEROS = 100
suma = 0
for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingresá el número {i+1}: "))
    suma += numero
media = suma / CANTIDAD_NUMEROS
print("\nLa media de los números ingresados es:", media)

#Ejercicio 10
numero = input("Ingresá un número entero: ")
numero_invertido = numero[::-1]
print("El número invertido es:", numero_invertido)