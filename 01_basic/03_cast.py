###
# 03_type casting
###

print('Conversión de tipos')
print(type('100'))
print(type (int('100')))
print("convierte float a int siempre redondeando hacia abajo: 3.14", int(3.14), sep=' = ')
print("convierte float a int siempre redondeando hacia abajo: 3.99", int(3.99), sep=' = ')
print("Conversión a booleano: 1", bool(1), sep=' = ')
print("Conversión a booleano: 0", bool(0), sep=' = ')
print("Conversión a booleano: -1", bool(-1), sep=' = ')
print("Conversión a booleano: 0.0", bool(0.0), sep=' = ')
print("Conversión a booleano: -0.301", bool(0.301), sep=' = ')
print("Conversión a booleano: ''", bool(''), sep=' = ')
print("Conversión a booleano: ' '", bool(' '), sep=' = ')
print("Conversión a booleano: '0'", bool('0'), sep=' = ')