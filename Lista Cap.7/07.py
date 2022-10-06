def calc_menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    elif n3 < n1 and n3 < n2:
       return n3

def calc_media_segundo(n1, n2, n3, n4, n5):
    maior = n1
    if (n2 > maior):
        maior = n2
    elif (n3 > maior):
        maior = n3
    elif (n4 > maior):
        maior = n4
    elif (n5 > maior):
        maior = n5
    
    menor = n1
    if (n2 < menor):
        menor = n2
    if (n3 < menor):
        menor = n3
    if (n4 < menor):
        menor = n5
    if (n5 < menor):
        menor = n5
    soma_total = n1+n2+n3+n4+n5
    soma_notas_selecionadas = soma_total - (maior+menor)
    return soma_notas_selecionadas
    
def calc_prim(l, n1, n2, n3):
    menor = calc_menor(n1, n2, n3)
    soma = (n1+n2+n3)-menor
    l = l*0.50
    soma = soma*0.50
    return l+soma
    

def calc_segundo(l, n1, n2, n3, n4, n5):
    l = l*0.20
    notas_selec = calc_media_segundo(n1, n2, n3, n4, n5)
    media = l+(notas_selec*0.80)
    return media
    

l, a1, a2, a3 = map(int,input().split())
l2, b1, b2, b3, b4, b5 = map(int,input().split())
b1 = calc_prim(l, a1, a2, a3)
b2 = calc_segundo(l2, b1, b2, b3, b4, b5)
m = (b1*2+b2*3)/5

if m>=60:
    print("APROVADO")
else:
    print("reprovado")