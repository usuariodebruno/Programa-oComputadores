a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    maior = a 
elif b > a and b>c:
    maior = b 
elif c > a and c>b:
    maior = c
soma_menores = (a+b+c)-maior
if soma_menores > maior:
    if a == b and a == c and b == c:
        print("equilatero")
    elif a == b or a == c or b == c:
        print("isosceles")
    elif a != b or a != c or b != c:
         print("escaleno")
else:
    print("Nenhum")