import psutil
import platform
import cpuinfo

sistema_operacional =  platform.system()
sistema_operacional_2 = platform.release()

lista_processador = cpuinfo.get_cpu_info()
for i, marca in lista_processador.items():     
    if i == 'brand_raw':
        processador = marca

'''solução temporária possivelmente eterna
explicação: como o que era armazenado era uma grande classe (classe é uma variável seguida de um valor, como: 'cpuinfo_version': [9, 0, 0]),
portanto eu fiz um for onde o i percorre a variável e a marca percorre o valor, então quando a variável fosse a brand_raw, que é a variável que
armazenava o valor que eu queria, eu armazenava esse valor em ula variável para usar posteriormente.

sim, o .items() não fica colorido mas sem ele é tanta informação que crasha o debug'''

memoria = psutil.virtual_memory()
memoria_GB = memoria.total / 1024 ** 3
memoria_livre = memoria.available / 1024 ** 3
armazenamento= psutil.disk_usage('/')
disk_gb= armazenamento.total / 1024 ** 3
disk_free= armazenamento.free / 1024 ** 3
disk_used= armazenamento.used / 1024 ** 3

def barra():
    print('-------------------------------------')

while True:
    print('QUAIS INFORMÇÔES DO SEU PC DESEJA SABER?')
    print("---------------MENU---------------------")
    print('Digite "1" para obter informações do seu Sistema Operacional.')
    barra()
    print('Digite "2" para obter informações do seu Processador.')
    barra()
    print('Digite "3" para obter informações da sua Memória RAM.')
    barra()
    print('Digite "4" para obter informações de armazenamento(HD/SSD).')
    barra()
    print('Digite "5" para sair.')
    barra()
    print("\n")
    n = int(input("Digite aqui o número da alternativa que deseja saber:"))
    while n < 1 or n > 5:
        n = int(input("OPÇÃO INVÁLIDA!! /Digite um opção válida!"))     
    if n == 1:
        print(f"{sistema_operacional} é seu Sistema Operacional e {sistema_operacional_2} é a sua versão.")   
        print("\n")          
        continue
    elif n == 2:
        print(f"Este é o seu Processador: {processador}")
        print("\n")
        continue
    elif n == 3:
        print(f"Seu PC tem {round(memoria_GB)} GB de Mémoria RAM e {round(memoria_livre)} GB de Memória Livre")
        print("\n")        
        continue
    elif n == 4:
        print(f'Armazenamento: {disk_gb:,.2f} gigas total, {disk_used:,.2f} em uso, {disk_free:,.2f} disponível. ')
        print("\n")
        continue
    else:
        break