#sumar dos numeros
import os
os.system("cls || clear")
os.system("color a4")
try: 
    num1 = eval(input("por favor dime un numero:"))
    num2 = eval (input("por favor dimer otro numero:"))
    suma = num1 + num2

    print ("La suma ees:", suma)
except Exception as ex:
    os.system ("color cf")
    
