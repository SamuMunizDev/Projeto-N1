import random
sala = 1
jogadas = 0
LIMITE_JOGADAS = 7
print('''Bem vindo ao game''')
print('''Para iniciar voce deve escolher um dos dois caminhos: [1] vermelho ou [2] preto: ''')


while(jogadas < LIMITE_JOGADAS and sala != 9):
    print('''Voce esta na sala: {}'''.format(sala))

    jogadas = jogadas + 1

    caminho = int(input("1 para vermelho e 2 para preto: "))

    while(caminho < 1 or caminho > 2):
        caminho = int(input("Digitou errado --- 1 para vermelho e 2 para preto: "))

    while(caminho == 1 or caminho == 2):
        if(caminho == 1):
            sala = sala + 1
        elif(caminho == 2 and sala == 8):
            print("Você caiu na sala 8 e sera teleportado para um novo lugar!!!")
            sala = random.randint(1,5)

        else:
             sala = sala + 2

        break

if(sala == 9):
    print('''Voce esta na sala: {}'''.format(sala))
    print("Parabens voce ganhou!! ")
else:
    print('''Voce esta na sala: {}'''.format(sala))
    print("Voce ultrapassou o limite de jogadas 😦  Game Over!!")