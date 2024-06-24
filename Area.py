# Área del cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))
area_cuadrado = lado ** 2
print("Área del cuadrado:", area_cuadrado)

# Área del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area_rectangulo = base * altura
print("Área del rectángulo:", area_rectangulo)

# Área del triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = (base * altura) / 2
print("Área del triángulo:", area_triangulo)

# Área del rombo
diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
area_rombo = (diagonal_menor * diagonal_mayor) / 2
print("Área del rombo:", area_rombo)