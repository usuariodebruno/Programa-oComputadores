def conta_digitos(n,d):
    d1 = str(d)
    if d1 == '10': return 0
    else:
        print(f'{d1}: {n.count(d1)}')
        return conta_digitos(n,d+1)

n = input()
conta_digitos(n,0)