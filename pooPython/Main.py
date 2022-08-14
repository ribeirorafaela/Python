class Main:
    pass

from Cliente import Cliente
from Conta import Conta

c1= Cliente("João","3212-3251")

conta = Conta (c1._nome, 1222)

conta.deposito (100)
conta.saque(50)
conta.extrato()