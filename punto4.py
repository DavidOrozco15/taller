import os

os.system("clear")

print("Bienvenido al programa para calcular el promedio de 5 notas")

nota1 = float(input("Introduce la primera nota: "))
nota2 = float(input("Introduce la segunda nota: "))
nota3 = float(input("Introduce la tercera nota: "))
nota4 = float(input("Introduce la cuarta nota: "))
nota5 = float(input("Introduce la quinta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (promedio) >= 3.5:
    print(f"El estudiante aprobó con un promedio de: {promedio}")
else:
    print(f"El estudiante reprobó con un promedio de: {promedio}")
    
    # made by Leonardo Vanegas and Juan Gamboa         