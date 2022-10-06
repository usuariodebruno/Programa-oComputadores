def exp(a, e ):
    if (e==0):
        return 1
    else:
        return a*exp(a,e-1)

a, e = map(int,input().split())
if a >= 0 and e >= 0:
    y = exp(a,e)
    print("{:d} elevado a {:d}= {:d}".format(a, e, y))
else:
    print("numero informado é negativo")