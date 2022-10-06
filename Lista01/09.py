dias = int(input())
s = 0
d = 0
while dias >= 7:
    s = s+1
    dias = dias-7
    
    
while d != 0:
    d = d+1
    dias = dias-1

print(f"{s} semana(s) \n{d} dia(s)")
