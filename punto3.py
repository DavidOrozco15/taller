import os

os.system("clear")

print("Bienvenido al programa del numero mayor")

numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))
numero3 = float(input("Introduce el tercer numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3
    
print(f"El numero mayor es: {mayor}")    

# made by Leonardo Vanegas and Juan Gamboa         
1