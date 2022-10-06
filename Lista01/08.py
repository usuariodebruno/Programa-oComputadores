inicio = int(input())
fim = int(input())
t = fim - inicio
h = 0
m = 0
while t >= 60:
    h = h+1
    t = t-60
    
    
while t != 0:
    m = m+1
    t = t-1

print(f"{h}:{m}")
