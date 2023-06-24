import platform
import cpuinfo
import psutil
r= " "

while r != "N":
    menu=int(input("[1] para saber o sistema operacional.\n[2] para saber nformações do processador.\n[3] para saber nformações de memória.\n[4] para saber nformações de armazenamento (tamanho do HD e SSD).\n[5] para sair do programa.\n Qual sua opção? " ))
    while menu > 5 or menu  < 1:
        print("NÚMERO INVÁLIDO TENTE NOVAMENTE ")
        menu=int(input("[1] para saber o sistema operacional.\n[2] para saber nformações do processador.\n[3] para saber nformações de memória.\n[4] para saber nformações de armazenamento (tamanho do HD e SSD).\n[5] para sair do programa.\n Qual sua opção?" ))
    
    if menu == 1 :
        print(f"o sistema operacional do seu computador é {platform.system()} e a sua versão é {platform.release()} ")
        r=str(input("Quer continuar [S/N]")).upper()
    if menu == 2:
        processador =cpuinfo.get_cpu_info_json()
        print(f" o seu processador é um {processador}")
        r=str(input("Quer continuar [S/N]")).upper()
    if menu == 3:
        mem = psutil.virtual_memory()
        mem_RAM = mem.total / 1024 ** 3
        print(f" voce tem memória GB {mem}")
        r=str(input("Quer continuar [S/N]")).upper()
    if menu == 4:
        armazenamento = psutil.disk_usage
        print(f"informações sobre o armazenamento {armazenamento}")
        r=str(input("Quer continuar [S/N]")).upper()
    while r not in "SN":
        print("LETRA INVÁLIDA TENTE NOVAMENTE")
        r=str(input("Quer continuar [S/N]")).upper()