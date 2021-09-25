import random
sala = 1
jogadas = 0
LIMITE_JOGADAS = 7

print('''Olá jovem guerreiro(a), bem vindo(a) ao mundo de Britannia!
Antes de começarmos sua jornada devemos sair desta dungeon.
Você deve guiar seus companheiros para o final deste temível labirinto.
Sinto em você o potencial para chegar até o final!
Agora vamos, antes que aqueles malditos goblins cheguem... 
''')
print('''Para iniciar você deve escolher um dos dois caminhos a frente, vermelho ou preto: ''')


while(sala != 9):
    print('''Voce está na sala: {}'''.format(sala))

    jogadas = jogadas + 1

    caminho = int(input('''[1] para o caminho vermelho e [2] para o caminho preto: 
    '''))

    while(caminho < 1 or caminho > 2):
        caminho = int(input('''Existem apenas dois caminhos, escolha novamente com mais sabedoria..
[1] para o caminho vermelho e [2] para o caminho preto:
     '''))

    while(caminho == 1 or caminho == 2):
        if(caminho == 1 and sala != 6):
            sala = sala + 1
        elif(caminho == 2 and sala == 8):
            print('''Acorde jovem mestre! Fomos levados por criaturas místicas que dominam o tempo-espaço,
eles criaram um portal e nos teleportaram para outra sala!!!''')
            sala = random.randint(1,5)

        else:
             sala = sala + 2

        break

if(sala == 9 and jogadas < LIMITE_JOGADAS):
        print('''Voce esta na sala: {}'''.format(sala))
        print('''Parabens jovem mestre, saímos daquele lugar estranho.
Agora você pode se aventurar pelo mundo com seus companheiros!! ''')
else:
        print('''Voce está na sala: {}'''.format(sala))
        print('''Mas chegamos tarde demais e infelizmente nossa missão fracassou... 
    Game Over!''')