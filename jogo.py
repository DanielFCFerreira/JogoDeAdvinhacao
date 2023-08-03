import random

print("**********************************")
print("**Bem vindo ao jogo de Advinhação**")
print("**********************************")

numero_secreto = round(random.randrange(1, 101))
tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("Define o nível: "))

if nivel == 1:
    print("Dificuldade Fácil")
    tentativas = 20
elif nivel == 2:
    print("Dificuldade Média")
    tentativas = 10
else:
    print("Dificuldade Difícil")
    tentativas = 5

for rodada in range(1, tentativas + 1):

    print(f"Rodada {rodada} de {tentativas}")
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou " , chute)

    if(chute < 1 or chute >100):
        print("Você precisa digitar um número entre 1 e 100")
        continue


    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto

    if acertou:
        print("**********************************")
        print("****Parabéns você acertou!!!!!!***")
        print(f"****Você fez {pontos} pontos***********")
        print("**********************************")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
