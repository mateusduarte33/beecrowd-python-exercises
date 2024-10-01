numero1 = float(input())
numero2 = float(input())
numero3 = float(input())
numero4 = float(input())
numero5 = float(input())
numero6 = float(input()) 

numeroPositivo = 0
SomaPositivo = 0.0

if numero1 > 0: 
    numeroPositivo +=1 
    SomaPositivo +=numero1

if numero2 > 0: 
    numeroPositivo +=1
    SomaPositivo +=numero2


if numero3 > 0: 
    numeroPositivo +=1
    SomaPositivo +=numero3


if numero4 > 0: 
    numeroPositivo +=1
    SomaPositivo +=numero4


if numero5 > 0: 
    numeroPositivo +=1
    SomaPositivo +=numero5

if numero6 > 0: 
    numeroPositivo +=1
    SomaPositivo +=numero6

    
    
media = SomaPositivo / numeroPositivo


 
 
print(f'{numeroPositivo} valores positivos')
print(f'{media:.1f}')
