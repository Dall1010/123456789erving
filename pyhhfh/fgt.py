#elevar al cuadrado  un numero

import os

os.system("cls || clear")
os.system("color a4")

try:
    number = int(input("Dime un numero:"))
    cuadrado = pow(number, 2)
    print("El cuadrado es", cuadrado)
except Exception as ex:
    os.system ("color cf")
    print("Error no se puede calcular numeros flotantes")
    


