import os

os.system("clear")

isActive = True
while isActive:
    os.system("clear")
    print("Bienvenido al programa para imprimir un triángulo de '*'")
    try:
        base = int(input("Introduce la base del triángulo: "))
        print("Oprime 0 para salir")
        if base == 0:
            isActive = False
        elif base < 0:
            for i in range(1, base + 1):
                print('*' * i)
            input("Presiona Enter para continuar...")
        else:
            print("No Existe un triangulo con base 1")
            os.system("clear")
            
    except ValueError:
        print("Por favor, introduce un número entero válido.")
        input("Presiona Enter para continuar...")
            
            # made by Leonardo Vanegas and Juan Gamboa         