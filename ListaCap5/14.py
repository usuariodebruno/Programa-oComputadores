dia, mes,ano = map(int,input().split())

if mes == 2 and dia < 28:
    print("Valida")
    if(dia>= 1 and dia <=28):
        if(dia==28):
            dia = 1
            mes = 3
            print(dia,"/",mes,"/",ano)
        else:
            print(dia+1,"/",mes,"/",ano)
            
elif mes == 4 or mes ==6 or mes == 9 or mes == 11 and dia <= 30:
    print("Valida")
    if(dia>= 1 and dia <=30):
        if(dia==30):
            dia = 1
            mes = mes + 1
            print(dia,"/",mes,"/",ano)
        else:
            print(dia+1,"/",mes,"/",ano)
            
            
elif mes == 1 or mes == 3 or mes ==5 or mes ==7 or mes ==8 or mes == 10 or mes == 12 and  dia <= 31:
     print("Valida")
     if(dia>= 1 and dia <=31):
        if(dia==31):
            dia = 1
            mes = mes+1
            print(dia,"/",mes,"/",ano)
        else:
            print(dia+1,"/",mes,"/",ano)
else: 
    print("Data Inválido")

    
