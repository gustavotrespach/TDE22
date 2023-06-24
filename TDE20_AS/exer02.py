import random as r
import io

pontos_j_1 = []
pontos_j_2 = []

vitorias_j_1 = 0
vitorias_j_2 = 0

nome_j_1 = str(input("Digite o nome do jogador 1: "))
nome_j_2 = str(input("Digite o nome do jogador 2: "))

for i in range(1,11):
    enter = str(input("Pressione enter para iniciar a próxima rodada."))

    j_1 = r.randint(1,6)
    j_2 = r.randint(1,6)
    
    pontos_j_1.append(j_1)
    pontos_j_2.append(j_2)

    if i == 1:
        with io.open('exer02.txt', 'w') as file:
            file.write(f"Rodada {i}\n{nome_j_1}: {j_1}\n{nome_j_2}: {j_2}\n")
    else:
        with io.open('exer02.txt', 'a') as file:
            file.write(f"\nRodada {i}\n{nome_j_1}: {j_1}\n{nome_j_2}: {j_2}\n")
    
    if j_1 == j_2:
        print(f"\n{nome_j_1}: {j_1}\n{nome_j_2}: {j_2}\nHouve um empate na rodada {i}\n")
    elif j_1 > j_2:
        print(f"\n{nome_j_1}: {j_1}\n{nome_j_2}: {j_2}\n{nome_j_1} venceu a rodada {i}.\n")
        vitorias_j_1 += 1
    else:
        print(f"\n{nome_j_1}: {j_1}\n{nome_j_2}: {j_2}\n{nome_j_2} venceu a rodada {i}.\n")
        vitorias_j_2 += 1

print(f"Pontuação de {nome_j_1}: {sum(pontos_j_1)}\nPontuação de {nome_j_2}: {sum(pontos_j_2)}")

if sum(pontos_j_1) > sum(pontos_j_2):
    print(f"        *              *              *                     *\n   *       *     Jogador Campeão: {nome_j_1} - pontuação: {sum(pontos_j_1)}     *       *   \n        *              *              *                     *\n")
elif sum(pontos_j_1) < sum(pontos_j_2):
    print(f"        *              *              *                     *\n   *       *     Jogador Campeão: {nome_j_2} - pontuação: {sum(pontos_j_2)}     *       *   \n        *              *              *                     *\n")
else:
    if vitorias_j_1 > vitorias_j_2:
        print(f"        *              *              *                     *\n   *       *     Jogador Campeão: {nome_j_1} - pontuação: {sum(pontos_j_1)} e vitórias: {vitorias_j_1}     *       *   \n        *              *              *                     *\n")
    elif vitorias_j_1 < vitorias_j_2:
        print(f"        *              *              *                     *\n   *       *     Jogador Campeão: {nome_j_2} - pontuação: {sum(pontos_j_2)} e vitórias: {vitorias_j_2}     *       *   \n        *              *              *                     *\n")
    else:
        print("Foi um empate completo!")