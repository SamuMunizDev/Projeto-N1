sala = 1
jogadas = 0
LIMITE_JOGADAS = 7
caminho = 1
print('''Bem vindo ao game''')
print('''Voce esta na sala: {}'''.format(sala))
print('''Para iniciar voce deve escolher um dos dois caminhos: [1] vermelho ou [2] preto''')

caminho = int(input("Escolha 1 para vermelho e 2 para preto:"))

if(caminho == 1):
    sala = sala + 1
    print("Voce esta na sala: {}".format(sala))

elif(caminho == 2):
        sala = sala + 2
        print("Voce esta na sala: {}".format(sala))
else:
    print("Escolha Invalida")

jogadas = jogadas + 1

print("voce jogou {} vezes".format (jogadas))