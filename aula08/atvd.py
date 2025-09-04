import random
import os

def escolher_palavras():
    palavras = ['flamengo', 'paysandu', 'remo', 'mirassol', 'bahia', 'cruzeiro', 'sport', 'santos', 'figueirense',
            'avai', 'vasco', 'america', 'fortaleza', 'goias', 'palmeiras', 'corinthians', 'gremio',
            'nautico', 'vitoria', 'ceara']
   
    return random.choice(palavras)



def jogar_forca():
    palavra= escolher_palavras()
    letras_corretas= []
    letras_erradas= []  
    tentativas= 6

    while True:
        palavra_escondida= ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'

        print('Palavra:', palavra_escondida)
        print('Letras erradas:', letras_erradas)
        print('Tentativas restantes:', tentativas)

        if palavra_escondida == palavra:
            print('Parabéns! Você ganhou!')
            break
        elif tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)
            break

        letra_usuario= input('Digite uma letra: ').lower()

        if letra_usuario in palavra:
            print('Letra correta!')
            letras_corretas.append(letra_usuario)
        else:
            print('Letra errada!')
            letras_erradas.append(letra_usuario)
            tentativas -= 1

if __name__ == "__main__":
    os.system('cls')
    print("Bem-vindo ao jogo da Forca!")
    jogar_forca()
