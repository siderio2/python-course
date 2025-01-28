##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Asignar una variable
# solo hace falta poner esto
my_name = "midudev"
# print(my_name)

age = 32
# print(age)

# Reasignar una variable: se puede hacer en tiempo de ejecución
# age = 39
# print(age)

# Tipado dinámico: el tipo de dato se determine en tiempo de ejecución
# que no tienes que declararlo explícitamente
name = "midudev"
# print(type(name))

name = 32 
# print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipo automáticas
# print(10 + "2")

# f-string (literal de cadena de formato)
# desde la versión Python 3.6
print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
name, age, city = "midudev", 32, "Bogotá"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

miNombreDeVariable = "no-recomendado" # camelCase
MiNombreDeVariable = "no-recomendado" # PascalCase
minombredevariable = "no-recomendado" # todo junto

mi_nombre_de_variable_123 = "ok"

# UPPER_CASE -> constantes 'fake'. PYTHON NO TIENE CONSTANTES, ES UNA CONVENCIÓN
MI_CONSTANTE = 3.14

# nombres no válidos de variables
# 123123_variable = "ko"
# mi-variable = "ko"
# mi variable = "ko"

# True = False

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# los tipos pueden anotarse (type annotation). Esto no afecta al comportamiento de
# la variable con respecto al funcionamiento del propio lenguaje
is_user_logged_in: bool = True
print(is_user_logged_in)

# Pero si podemos activar la opción Type Checking dentro del IDE
# y ver errores de tipado, incluso con efecto 'hoisting'
# is_user_logged_in = "no"
# name: str = "midudev"
print(is_user_logged_in)