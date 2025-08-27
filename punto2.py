import os
os.system("clear")
print("Tabla de multiplicar")

isActive = True

while isActive:
    numero = float(input("Introduce un número para ver su tabla de multiplicar: "))
    if 1 <= numero <= 10:  
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
        input("\nPresiona Enter para continuar...")
        os.system("clear")  
    else:
        print("Introduce un número entre 1 y 10")
        input("Presiona Enter para continuar...")
        os.system("clear")  
            
              




# made by Leonardo Vanegas and Juan Gamboa         