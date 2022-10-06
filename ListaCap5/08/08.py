a = int(input())
b = int(input())
c = int(input())
menor = a

if a < b:
    menor = a 
elif a < c:
    menor = a
elif b < a:
    menor = b
elif b < c:
    menor = b
elif c < a:
    menor = c
elif c < b:
    menor = c
print(menor)