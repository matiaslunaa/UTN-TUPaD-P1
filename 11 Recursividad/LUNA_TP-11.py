#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresá un número entero positivo: "))
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

#Ejrecicio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
posicion = int(input("Ingresá una posición: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero = int(input("Ingresá un número entero positivo: "))
if numero < 0:
    print("Ingresá un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
palabra = input("Ingresá una palabra sin espacios ni tildes: ").lower()
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')

#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
numero = int(input("Ingresá un número entero positivo: "))
if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
n = int(input("Ingresá el número de bloques del nivel más bajo: "))
if n < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    total = contar_bloques(n)
    print(f"Para construir la pirámide se necesitan {total} bloques en total.")

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("¿Qué dígito querés contar (0 al 9)?: "))
if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. Asegurate de que el número sea positivo y el dígito esté entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")