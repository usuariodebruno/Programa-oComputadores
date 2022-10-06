def fat(n ):
    if (n==0):
        return 1
    else:
        return n*fat(n-1)

n, n2 = map(int,input().split())

if n >= 0 and n2 >= 0:
    print(fat(n)+fat(n2))
else:
    print("numero informado é negativo")