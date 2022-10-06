a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a > b and a > c and a > d and a > e:
    maior = a 
elif b > a and b>c and b>d and b>e:
    maior = b 
elif c > a and c>b and c>d and c>e:
    maior = c
elif d>a and d>b and d>c and d>e:
    maior = d
elif e>a and e>b and e>c and e>d:
    maior = e
print(maior)