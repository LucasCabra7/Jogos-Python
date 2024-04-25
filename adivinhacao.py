import random


def jogar():

    print("*********************************")
    print("Bem vindo ao Jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101, 1))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade você deseja?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Digite a dificuldade: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Por favor dígite a dificuldade!")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute)
        numero_chutado = int(chute)

        if(numero_chutado < 1 or numero_chutado > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == numero_chutado
        maior   = numero_secreto > numero_chutado
        menor   = numero_secreto < numero_chutado

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi menor do que o número secreto!")
            elif(menor):
                print("Você errou! O seu chute foi maior do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - numero_chutado)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar()



