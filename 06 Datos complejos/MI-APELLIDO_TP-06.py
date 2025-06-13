#Ejercicio 1
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())

print("Diccionario de precios actualizados:")
print(precios_frutas)
print("\nLista de frutas:")
print(lista_frutas)

#Ejercicio 4
contactos = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

buscar = input("\n¿A qué contacto querés buscar?: ")

if buscar in contactos:
    print(f"El número de {buscar} es {contactos[buscar]}")
else:
    print(f"No se encontró el contacto '{buscar}'")

#Ejercicio 5
frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("\nPalabras únicas:", palabras_unicas)
print("Recuento:", recuento)

#Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)

    alumnos[nombre] = tuple(notas)

print("\nPromedios de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio 7
parcial1 = {"Ana", "Luis", "Marta", "Carlos", "Sofía"}
parcial2 = {"Luis", "Sofía", "Juan", "Camila"}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
todos = parcial1 | parcial2
print("Aprobados en ambos parciales:", ambos)
print("Aprobados en solo uno:", solo_uno)
print("Aprobados en al menos uno:", todos)

#Ejercicio 8
stock_productos = {
    "Arroz": 20,
    "Fideos": 15,
    "Aceite": 10
}

print("\n Gestión de Stock")
producto = input("Ingresá el nombre del producto que querés consultar o modificar: ")

producto = producto.capitalize()
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")
    opcion = input("¿Querés agregar unidades?: ")
    if opcion.lower() == "s":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"{producto} no está en el stock.")
    opcion = input("¿Querés agregarlo?: ")
    if opcion.lower() == "s":
        cantidad = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} fue agregado con {cantidad} unidades.")
print("\n Stock final:")
for producto, cantidad in stock_productos.items():
    print(f"{producto}: {cantidad}")

#Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio"
}
dia = input("Ingresá el día que querés consultar: ").lower()
hora = input("Ingresá la hora: ")
clave = (dia, hora)
if clave in agenda:
    print(f"Actividad en {dia} a las {hora}: {agenda[clave]}")
else:
    print("No hay ninguna actividad registrada en ese horario.")

#Ejercicio 10
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario original:")
print(original)
print("\nDiccionario invertido:")
print(invertido)
