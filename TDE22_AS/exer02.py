import requests as rq

def ver_conexao():
    if conversor_real.status_code == 200:
        return True
    else:
        return False
def msg_erro():
    print("Erro ao obter taxa de câmbio.")


conversor_real = rq.get('https://api.exchangerate-api.com/v4/latest/BRL')

while True:
    print(f'\n=======*=====MENU=====*=======\n1 - converter Real para Dólar\n2 - converter Real para Euro\n3 - converter Real para Peso\n0 - sair\n=======*==============*=======')
    
    escolha = int(input('\nDigite qual conversão você quer fazer: '))
    while escolha < 0 or escolha > 3:       #verificador se o comando é válido
        escolha = int(input('Opção inválida, escolha uma opção da lista: '))
    
    data = conversor_real.json()
    
    if escolha == 1:
        if ver_conexao():
            taxa = data['rates']['USD']
            
            valor_em_real = float(input('Digite o valor em real que você deseja converter: '))
            while valor_em_real < 0:       #verificador se o valor é positivo
                valor_em_real = float(input('Digite um valor positivo: '))

            valor_convertido = valor_em_real * taxa
            print(f'\nValor em Real: {valor_em_real}\nValor em Dólar: {round(valor_convertido, 2)}\n')
            continue
        else:
            msg_erro()
    elif escolha == 2:
        if ver_conexao():
            taxa = data['rates']['EUR']

            valor_em_real = float(input('Digite o valor em real que você deseja converter: '))
            while valor_em_real < 0:       #verificador se o valor é positivo
                valor_em_real = float(input('Digite um valor positivo: '))

            valor_convertido = valor_em_real * taxa
            print(f'\nValor em Real: {valor_em_real}\nValor em Euro: {round(valor_convertido, 2)}')
        else:
            msg_erro()
    elif escolha == 3:
        if ver_conexao():
            taxa = data['rates']['ARS']

            valor_em_real = float(input('Digite o valor em real que você deseja converter: '))
            while valor_em_real < 0:       #verificador se o valor é positivo
                valor_em_real = float(input('Digite um valor positivo: '))

            valor_convertido = valor_em_real * taxa
            print(f'\nValor em Real: {valor_em_real}\nValor em Peso: {round(valor_convertido, 2)}')
        else:
            msg_erro()
    elif escolha == 0:
        break
