def calcula_area(l,p):
    area = l*p
    return area
    
def calcular_maior(t1,t2,t3,t4):
    if t1 > t2 and t1 > t3 and t1 > t4:
        return "A"
    elif t2 > t1 and t2 > t3 and t2 > t4:
        return "B"
    elif t3 > t1 and t3 > t2 and t3 > t4:
        return "C"
    elif t4 > t1 and t4 > t2 and t4 > t3:
        return "D"
        
largura1, profundidade1 = map(int,input().split())
largura2, profundidade2 = map(int,input().split())
largura3, profundidade3 = map(int,input().split())
largura4, profundidade4 = map(int,input().split())

a1 = calcula_area(largura1, profundidade1)
a2 = calcula_area(largura2, profundidade2)
a3 = calcula_area(largura3, profundidade3)
a4 = calcula_area(largura4, profundidade4)

print(calcular_maior(a1,a2,a3,a4))