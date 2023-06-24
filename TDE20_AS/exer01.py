import random as r
import datetime as d

numero = r.randint(0,20) #gerando número aleatório
tentativas = 3 #numero de tentativas

hora_inicio = d.datetime.now() #captação da hora de início

while tentativas > 0: #loop para contagem de tentativas
    chute = int(input("Tente adivinhar um número de 0 a 20: "))
    
    while chute > 20 or chute < 0: #loop para verificação se o chute é válido
        chute = int(input("O número deve estar entre 0 e 20: "))
    
    if chute > numero: 
        print("\n Chute muito alto, tente novamente.\n")
        tentativas -= 1
        continue
    elif chute < numero:
        print("\n Chute muito baixo, tente novamente.\n")
        tentativas -= 1
        continue
    else:
        print(f"Você acertou o número: {chute} !")
        break

if tentativas == 0:
    print(f"Acabaram suas tentativas, você não conseguiu adivinhar.\nSorteado: {numero}")

diferença = d.datetime.now() - hora_inicio #diferença dos horarios final e inicial

dif_segundos = diferença.total_seconds() #transformando a diferença em segundos para poder melhorar o print, puramente estética

if dif_segundos > 60: #if para fazer os cálculos de minutos e horas baseado nos segundos da variável anterior, puramente estética
    dif_minutos = dif_segundos // 60
    dif_segundos = dif_segundos % 60
else:
    dif_minutos = 0

if dif_minutos > 60:
    dif_horas = dif_minutos // 60
    dif_minutos = dif_minutos % 60
else:
    dif_horas = 0

segundos = round(dif_segundos,2) #variaveis finais para arredondar os valores e não aparecer nem o float dos minutos e nem os milisegundos, puramente estética
minutos = round(dif_minutos)
horas = round(dif_horas) 

print(f"Você ficou {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s) tentando acertar.")