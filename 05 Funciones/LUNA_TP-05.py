#TP Listas Unidad 5.1
#Ejercicio 1
multiplos_de_4 = list(range(4, 101, 4))
print("Los múltiplos de 4 del 1 al 100 son:")
print(multiplos_de_4)

#Ejercicio 2
marcas_de_autos = ["Peugeot", "Honda", "Audi", "BMW", "FIAT"]
print("Lista de autos:", marcas_de_autos)
print("La penúltima marca es: ", marcas_de_autos[-2])

#Ejercicio 3
lista_vacia = []
lista_vacia.append("CPU")
lista_vacia.append("Placa de video")
lista_vacia.append("Fuente")
print("Lista con las palabras agregadas:")
print(lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista actualizada de animales:")
print(animales)

#Ejercicio 5
#En este programa se crea una lista de numeros, que lo que hace es que busca el numero mas alto y elimina ese numero mas alto
#y por ultimo te devuelve la lista final sin el numero mas alto de esa lista de numeros.

#Ejercicio 6
numeros = list(range(10, 31, 5))
print("Los 2 primeros numeros son:", numeros[:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "mustang"
autos[2] = "camaro"
print("Lista actualizada de los autos:")
print(autos)

#Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista con los dobles de 5, 10 y 15:")
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista de compras:")
print(compras)

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:")
print(lista_anidada)



#Ejercicios Unidad 05 Funciones:
#Ejerecicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nomrbre):
    return f"Hola {nomrbre}!"
nombre_usuario = input("Ingresá tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad}, y vivo en {residencia}")
nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingresá el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = float(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma=a+b
    resta=a-b
    mul=a*b
    div=a/b
    tupla=(suma,resta,mul,div)
    print(type(tupla))
    return tupla

#Ejercicio 8
from math import pow
def calcular_imc(kilos,alt):
    imc=kilos/pow(alt,2)
    print(f"El imc es: {imc}")
kil=float(input("Ingresá tu peso: "))
al=float(input("Ingresá tu altura: "))
calcular_imc(kil,al)

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    far=celsius*9/5+32
    print(f"El equivalente a {celsius} grados celsius es {far} grados farenheit")
grados=float(input("Ingresá los grados: "))
celsius_a_fahrenheit(grados)

#Ejercicio 10
def calcular_promedio(a, b, c):
    print("El promedio de los tres números es: ",(a+b+c)/3)
num1=int(input("Ingresar número 1: "))
num2=int(input("Ingresar número 2: "))
num3=int(input("Ingresar número 3: "))
calcular_promedio(num1,num2,num3)