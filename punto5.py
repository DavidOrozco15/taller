import os

os.system("clear")

print("Bienvenido al programa para imprimir un triángulo de '*'")

base = int(input("Introduce el numero de '*' deseados para la base del triangulo: "))

for i in range(1, base+1):
    print("*"*i)