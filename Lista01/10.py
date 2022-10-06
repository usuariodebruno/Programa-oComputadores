valor_itens = int(input())
quantidades = int(input())
valor_cliente = int(input())

a_pagar = valor_itens*quantidades
valor_troco = valor_cliente-a_pagar

print(f" A pagar {a_pagar}  \nTroco {valor_troco} ")
