int_lista = list(map(int, []))
int_primos = list(map(int, [2, 3, 5, 7]))

def calcular_fatoracao(n):
    divisor = 2
    i = 0
    
    while n > 1: 
        if n%int_primos[i] == 0:
            n = n/int_primos[i]
            int_lista.append(int_primos[i])
        else:
            i =i+1
            
            
    return int_lista

numero = int(input())
lista_fatores = calcular_fatoracao(numero)
print(*lista_fatores, sep="x")