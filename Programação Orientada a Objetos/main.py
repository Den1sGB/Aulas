from conta import *
from cliente import *

if __name__ == '__main__':
    cliente1 = Cliente('Fabrício','Dias','000.000.000-00')
    conta1 = Conta('1234',cliente1,1000,5000)
    conta1.extrato()
    print("=========================")
    cliente1.exibir()
