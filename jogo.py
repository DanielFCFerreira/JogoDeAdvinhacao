import random

print("**********************************")
print("**Bem vindo ao jogo de Advinhação**")
print("**********************************")

numero_secreto = round(random.random() * 100)
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
        print("**********************************")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

