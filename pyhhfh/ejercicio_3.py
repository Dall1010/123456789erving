class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"se han depositado {cantidad} unidades.")
        else:
            print("La cantidad a depositar deber ser mayor que c$100")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"se han retirado {cantidad} C$.")
        else:
            print("saldo insuficiente.")
    def consultar_saldo(self):
        print(f"su saldo actual es: {self.__saldo}")

mi_cuenta = CuentaBancaria(2000)
mi_cuenta.consultar_saldo()

mi_cuenta.depositar(-500)
mi_cuenta.depositar(500)
