def emfrente
if(caminho == 1):
    sala = sala + 1
    print("Voce esta na sala: {}".format(sala))

elif(caminho == 2):
        sala = sala + 2
        print("Voce esta na sala: {}".format(sala))
else:
    print("Escolha Invalida")
emfrente = int(input("Escolha 1 para vermelho e 2 para preto:"))