# matematicas.py

print("Calculadora Básica")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nResultados:")

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")

if num2!= 0:
    print(f"División: {num1 / num2}")
else:
    print("Error: No se puede dividir entre cero")