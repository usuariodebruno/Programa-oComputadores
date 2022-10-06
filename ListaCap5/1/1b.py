n1 = float(input())
n2 = float(input())
media = 0.0
if 0.0 <= n1 and n2 >= 10.0 and 0.0 <= n2 and n2 >= 10.0:
    media = float((n1*2+n2*3)/5)
    if media>=6.0:
        print("Aprovado")
    else:
        print("Em recuperação")
else:
    print("informe um valor válido para ambas as notas")

print("{:.1f}".format(media))
