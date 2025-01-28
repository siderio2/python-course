###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
# name, city = input("Escribe tu nombre y ciudad\n").split()
# print(f"Así que vives en {city}, {name}.")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print("a es de tipo", type(a))
print("b es de tipo", type(b))
print("c es de tipo", type(c))
print("d es de tipo", type(d))
print("e es de tipo", type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
print(cadena, "es de tipo", type(cadena))
entero = int(cadena)
print(entero, "es de tipo", type(entero))
float = float(entero)
print(float, "es de tipo", type(float))
float2 = 3.99
print(float2, "es de tipo", type(float2))
entero2 = int(float2)
print(entero2, "es de tipo", type(entero2))
print("¿Que ocurre?", "Pues que perdemos .99 en la conversión, casi un 25%", sep='->\t')

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
my_name = "Desi"
my_age = 53
my_height = 1.70
print(f"Hola! Me llamo {my_name} y tengo {my_age} años, mido {my_height:.2f} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14159
print("pi =", pi)
rounded_pi = round(pi)
print("rounded_pi =", rounded_pi)
division = rounded_pi//2
print("division =", division)