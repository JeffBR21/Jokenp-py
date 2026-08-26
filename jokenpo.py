import random
from time import sleep
rj = 0
rm = 0
random.seed()
ultima_jogada_maquina = None
no = str(input("Digite seu nome: "))

print(f"Bem vindo ao jogo de jonkenpo, {no}!")
print("1 - Iniciar jogo")
print("2 - sair")

n1 = int(input("Escolha uma opção entre 1 e 2:"))

while n1:
    if n1 == 1:
        print("Escolha os numeros de 1 a 3")
        print("1 - pedra")
        print("2 - papel")
        print("3 - tesoura")
        print("4 - sair")
        n2 = int(input("Qual a sua escolha? "))

        if n2 == 4:
            print("Obrigado por jogar, saindo do jogo!")
            break

        opcoes_maquina = [1, 2, 3]
        if ultima_jogada_maquina is not None:
            opcoes_maquina.remove(ultima_jogada_maquina)
        r = random.choice(opcoes_maquina)
        ultima_jogada_maquina = r

        if r == n2:
            print("Jó")
            sleep(1)
            print("ken")
            sleep(1)
            print("po!")
            sleep(1)
            print("Sua escolha foi: ", n2)
            print("A escolha da maquina foi: ", r)
            print("Empate!")
        elif (n2 == 1 and r == 3 or n2 == 2 and r ==1 or n2 == 3 and r == 2 ):
            print("Jó")
            sleep(1)
            print("ken")
            sleep(1)
            print("po!")
            sleep(1)
            print("Você ganhou!")
            print("Sua escolha foi: ", n2)
            print("A escolha da maquina foi: ", r)
            rj += 1 
            print(f"Resultado do jogador vs a máquina {rj} x {rm}")
        else:
            print("Jó")
            sleep(1)
            print("ken")
            sleep(1)
            print("po!")
            sleep(1)
            print("Sua escolha foi: ", n2)
            print("A escolha da maquina foi: ", r)
            print("Você perdeu!")
            rm += 1 
            print(f"Resultado do jogador vs a máquina {rj} x {rm}")
            

    elif n1 == 2:
        print("Obrigado por jogar, Saindo do Jogo!")
        break
    
         
