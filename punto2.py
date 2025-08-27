import os
os.system("clear")
print("Tabla de multiplicar")

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

if 1 <= numero <= 10:  
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("El número debe estar entre 1 y 10.")        

print("Gracias por usar el programa de tablas de multiplicar.")