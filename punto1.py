import os


os.system("clear")

nombre = input("Ingresa tu nombre completo: ")
cc = int(input("Ingresa tu número de cédula: "))

os.system("clear")

print("1. COP → USD")
print("2. USD → JPY")
print("3. JPY → COP")
print("4. Salir")


option = int(input("Ingresa una de las 3 opciones: "))

match option:
    
    case 1:
        print("COP → USD")
        COP1 = float(input("Ingresa la cantidad de COP a convertir: "))
        USD1 = COP1 * 0.00025
        print(f"Señor/a  {nombre} con cédula {cc}, la conversión de ${COP1} COP a USD es: ${USD1} USD")
        
    case 2:
        print("USD → JPY")
        USD2 = float(input("Ingresa la cantidad de USD a convertir: "))
        JPY2 = USD2 * 147.29
        print(f"Señor/a  {nombre} con cédula {cc}, la conversión de ${USD2} USD a JPY es: ${JPY2} JPY")    
        
    case 3:
        print("JPY → COP")  
        JPY3 = float(input("Ingresa la cantidad de JPY a convertir: "))
        COP3 = JPY3 * 27.35
        print(f"Señor/a  {nombre} con cédula {cc}, la conversión de ${JPY3} JPY a COP es: ${COP3} COP")   
    
    case 4:
        print("Gracias por usar el conversor de monedas. ¡Hasta luego!")    
        
    case _:
        print("Opción no válida")    