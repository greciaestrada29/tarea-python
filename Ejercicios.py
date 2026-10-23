# EJERCICIO 1: CALCULADORA SIMPLE
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

try:
    division = numero1 / numero2
except ZeroDivisionError:
    division = "No se puede dividir por cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# EJERCICIO 2: CONVERSIÓN DE TEMPERATURAS

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"{temperatura_celsius} grados Celsius son equivalentes a {temperatura_fahrenheit} grados Fahrenheit.")


# EJERCICIO 3: ÁREA DE UN TRIÁNGULO

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2

print(f"El área del triángulo es: {area}")


# CÁLCULO ADICIONAL

_Base = 4
Altura = 9

print(_Base * Altura / 2)


# EJERCICIO 9: CALCULADORA DE DESCUENTOS

precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))

descuento = (porcentaje_descuento / 100) * precio_original
precio_final = precio_original - descuento

print(f"El precio final del producto es: {precio_final}")
