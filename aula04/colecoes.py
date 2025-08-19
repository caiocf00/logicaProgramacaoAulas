'''nomes_lista = ['fulano' , 'cicrano' , 'Beltrano', 'joana', 'Maria', 'Mariana']
nome = input('informe o nome que deseja:')

if nome in nomes_lista:
    print(nome)
else:
    print(f'{nome} não encontrado.')'''
# index para buscar elementos em uma lista, try tratamento de erros
'''indice = nomes_lista.index(nome)'''
#count contar a quantidade de vezes quantas vezes aparece
#alteração de valor na lista nomes_listas[0](indice) =  outro valor
'''nomes_lista = ['fulano' , 'cicrano' , 'Beltrano', 'joana', 'Maria', 'Mariana']
nome_alterar = input('Informe o nome que deseja alterar:')
nomes_lista[nomes_lista.index(nome_alterar)] = input('informe o novoo nome:')

for nome in nomes_lista:
    print(nome)'''

#tabuada

'''numero = int(input('Digite o numero:'))

for i in range (1,11):
    resultado = numero * i 
    print(f'{i} X {numero} = {resultado}')'''

#Contagem regressiva Importando bibliotecas aula 04 19/08/25

'''import os
from time import sleep

cont = input('Digite um numero inteiro')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'Contagem regressiva: {cont_int}...')
        sleep

except:
    ...'''

# importando bibliotecas 
'''
Programa: Sorteio V.1.0
Impotando bibliotecas 

random; escolha aleatoria
Descrição: sistema recebe o nome dos candidatos e realiza o sorteio'''

'''import random

nome1 = input('Digite o primeiro nome:')
nome2 = input('Digite o segundo nome:')
nome3 = input('Digite o terceiro nome:')
nome4 = input('Digite o quarto nome:')
nome5 = input('Digite o quinto nome:')

lista_nome = [nome1,nome2,nome3,nome4,nome5]

escolhido = random.choice(lista_nome)
print(escolhido)'''

'''Programa: Sorteio V.2.0
Impotando bibliotecas '''

'''import random

lista = []

sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair:')
    if nome_candidato != '':
        # append - adiciona o valor da variavel dentro da lista
        lista.append(nome_candidato)
    else:
        sair = True
        escolhido= random.choice(lista)

        print('O escolhido foi:')'''

#importando lib 
'''Programa: Sorteio V.2.0'''
'''import random
import os
import time 

lista_nomes = []
lista_sorteados= []

while True:
    nome= input('Digite o nome para o sorteio:')
    if nome:
        lista_nomes.append(nome)
    else:
        break

    while True:
        if lista_nomes:
            os.system('cls')
            escolhido = random.choice(lista_nomes)
            lista_sorteados.append(escolhido)
            

            print(f'O escolhido foi: {escolhido}')

            opcao = input('Deseja sortear outro nome? S-sim \n | N- Não \n ').lower
            os.system('cls')

            if opcao != 's':
                break
            else:
                print('Não há nomes para sorteios!')
                break
print('programa finalizado!')
print(f"Os sorteados foram {lista_sorteados}")'''


''' Programa: Adivinhação V.1.0 '''

#importando lib
'''from random import randint
print('Tente adivinhar o numero!')
num1 = int(input("Digite um numero:"))

num_secret = randint(1,10)

if num1== num_secret:
        print("parabens, você ganhou!")
else:
        print('Voce perdeu')
        print(f'O numero correto é {num_secret}')'''

#import lib 
'''import random 

numero_secreto= random.randint(1,100)

tentativas = 0
max_tentavias = 10
acertou= False

print(30*'-','Bem vindo ao adinhalogo', 30* '-')
print(f'Você tem {max_tentavias} tentativas para adivinhar o numero secreto')
print('Vamos começar?')

while tentativas < max_tentavias:  
    try:
        #entrada do usuario
        palpite = int(input('Digite seu palpite:'))

    except ValueError:
        print()'''


