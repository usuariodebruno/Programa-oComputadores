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
    print("maior")
else:
    print("nao maior")