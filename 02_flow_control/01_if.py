###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os
import time
os.system("clear")

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# JavaScript
# && -> and
# || -> or

# 🇻🇪 un pueblo de Valencia
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# 🇻🇪 un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

numero = 5
if numero: # True
  print("El número no es cero")

numero = 0
if numero: # False
  print("Aquí no entrará nunca")

nombre = ""
if nombre:
  print("El nombre no es vacío")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")


print("\nLa condición ternaria:")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
# print("\nPor favor, introduce dos números y yo te diré cual es el mayor o si son iguales:\n")

# os.system("clear")
primero = int(input("\nPrimer número: \n"))
segundo = int(input("Segundo número: \n"))

if primero > segundo:
  print(f"{primero} es mayor que {segundo}")
elif segundo > primero:
  print(f"{segundo} es mayor que {primero}")
else:
  print("Los números son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# os.system("clear")
print("Hello.\n")
time.sleep(1)
print("Puedes llamarme Dora, Cálcula Dora.\n")
time.sleep(3)
print("Voy a pedirte dos operandos, un tipo de operación, y al final te daré el resultado.\n ")
time.sleep(3)
primer_operando = float(input("Primer operando: \n"))
operador = input("Tipo de operación (+ - * /)\n")
segundo_operando = float(input("Segundo operando: \n"))
division_por_cero = False
resultado = 0.0

if (operador == "+"):
  resultado = primer_operando + segundo_operando
elif (operador == "-"):
  resultado = primer_operando - segundo_operando
elif (operador == "*"):
  resultado = primer_operando * segundo_operando
elif (segundo_operando == 0.0):
  print("\nNo se puede realizar la operación: la división por cero no es posible")
  division_por_cero = True
else:
  resultado = primer_operando / segundo_operando

if (not division_por_cero):
  print(f"\n{primer_operando} {operador} {segundo_operando} = {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# os.system("clear")
an = int(input("Introduce un año: \n"))
es_bisiesto = True
if (an % 4 != 0 or (an % 100 == 0 and an % 400 != 0)):
  es_bisiesto = False

resultado = "es bisiesto 👌" if es_bisiesto else "no es bisiesto 👎"
print(f"{an} {resultado}")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# os.system("clear")
edad = int(input("A ver, criatura, introduce una una edad:\n"))
es_un = ""

if (edad <= 2):
  es_un = "bebé"
elif (edad <= 12):
  es_un = "niño"
elif (edad <= 17):
  es_un = "adolescente"
elif (edad <= 64):
  es_un = "adulto"
else:
  es_un = "adulto mayor"

print(f"Es un {es_un}")