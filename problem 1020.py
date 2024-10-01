age = int(input())

anos = age//365
meses = (age %  365)//30
dias = (age % 365) % 30
 
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
 
