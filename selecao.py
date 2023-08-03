import adivinhacao
import forca

print("**********************************")
print("**Bem vindo ao menu dos jogos**")
print("**********************************")
print("")
print("Qual jogo você quer jogar?")
jogo = int(input("(1) Adivinhação ou (2) Forca? "))

while True:
    if jogo == 1:
        adivinhacao.jogar()
    elif jogo == 2:
        forca.jogar()
    else:
        print("Escolha uma opção válida")
