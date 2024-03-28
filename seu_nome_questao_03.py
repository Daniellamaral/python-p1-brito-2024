# Questão 03 [1,5 pts (entrega) + 1,5 pts (oral)]

# Para doar sangue é necessário:
#  1. Ter entre 16 e 69 anos.
#  2. Pesar mais de 50 kg.
#  3. Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).
# 
#  Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24h
#  para uma pessoa e diga se ela pode doar sangue ou não.
# Programa para verificar se uma pessoa pode doar sangue

# Pergunta a idade, o peso e o tempo de sono nas últimas 24 horas
idade = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso em kg? "))
sono_horas = float(input("Quantas horas você dormiu nas últimas 24 horas? "))

# Verifica se a pessoa atende aos requisitos para doar sangue
if 16 <= idade <= 69 and peso > 50 and sono_horas >= 6:
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue.")
