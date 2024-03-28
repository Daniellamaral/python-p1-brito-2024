# Questão 04 [1,5 pts (entrega) + 1,5 pts (oral)]

#  Um restaurante que enfrenta problemas com sua capacidade de clientes
#  pediu sua ajuda para fazer um programa para saber quando eles atingem sua
#  capacidade máxima. Faça um programa que leia um número inteiro da capacidade
#  máxima do restaurante, e depois pergunte e leia a quantidade de clientes que
#  chegaram até ocupar toda a capacidade do restaurante e quando lotar imprima na
#  tela «Restaurante lotado, não há mais mesas disponíveis»
# Lê a capacidade máxima do restaurante
capacidade_maxima = int(input("Digite a capacidade máxima do restaurante: "))

# Variável para controlar a quantidade de clientes
clientes_atual = 0

# Loop para verificar se o restaurante está lotado
while clientes_atual < capacidade_maxima:
    # Lê a quantidade de clientes que chegaram
    clientes_chegaram = int(input("Quantos clientes chegaram? "))

    # Atualiza o número total de clientes
    clientes_atual += clientes_chegaram

    # Verifica se o restaurante está lotado
    if clientes_atual >= capacidade_maxima:
        print("Restaurante lotado, não há mais mesas disponíveis.")
        break  # Sai do loop se o restaurante estiver lotado
