 
N = int(input())

horas = N  // 3600
minutos = (N//60) % 60
segundos = N % 60

print(f'{horas:.0f}:{minutos:.0f}:{segundos:}')