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