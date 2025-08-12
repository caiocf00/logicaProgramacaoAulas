# concatenaçao

# cd .. volta para pasta anterior, cd(nome da pasta) abri uma pasta

#FIXME -  concatenaçao com +
'''
nome= 'Caio' 
idade = 19
altura = 1.75
''''''
print("Olá, meu nome é ," + nome + ", tenho " + str(idade) + " anos e minha altura é " + str(altura) + " metros.")

#FIXME -  concatenaçao com ,

print("Olá, meu nome é ,", nome ,", tenho ",idade ," anos e minha altura é ",altura," metros.")

#FIXME -  concatenaçao com format

print("Olá, meu nome é , {} , tenho {} anos e minha altura é {} metros." .format(nome, idade, altura))

#FIXME -  concatenaçao com fstrings

print(f"Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros.") 

# eliminando quebra de linha
print("O sabio sabia", end=" ")
print("que sabia sabia assobiar")

valor = 1.222223
#exibindo o valor com 2 casas decimais
print(f"{valor:,.2f}")

print(30*"=")
peso = input("Digite seu peso: ").replace(",",".")
peso = float(peso)
print(peso)
'''
'''


soma1 = 12
soma2 = 7
expo1 = 3
expo2 = 2
div1= 15
div2 = 4
soma = soma1 + soma2
expo = expo1 ** expo2
divisao = div1 / div2
print("Resultado da soma", soma1, "+", soma2, "=", soma)
print("Resultado da exponenciação", expo1, "**", expo2, "=", expo)
print("Resultado da divisão", div1, "/", div2, "=", divisao)
'''

# Exemplo de uso de if-else
''''
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if idade >= "18":
    print(f"{nome}, você é maior de idade.")    

else:
    print(f"{nome}, você é menor de idade.")

    num1 = 10 

    if num1 %2 == 0: 
        print("O número é par")     
    else:
        print("O número é ímpar")
'''
'''print(30*"-","BOLETIM ESCOLAR DO ANDRÉ",30*"-") # upper = Caixa altas, lower = caixa baixa
aluno = input("Digite o nome do aluno: ").upper()
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))    
nota3 = float(input("Digite a primeira nota: "))
nota4 = float(input("Digite a primeira nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

# >= 7 aprovado
# >= 5  recuperação
# reprovado
if media >= 7:
    print(f'{aluno}!!1 Aluno aprovado!')
    print(f'Nota 1: {nota1}/ Nota 2: {nota2}/ Nota 3: {nota3}/ Nota 4: {nota4}')
    print(20*'-')
    print(f'Média: {media}')

elif media >= 5:
    print(f'{aluno} Aluno em recuperação!')
    print(f'Nota 1: {nota1}/ Nota 2: {nota2}/ Nota 3: {nota3}/ Nota 4: {nota4}')
    print(20*'-')
    print(f'media : {media}')        
else:
    print(f'{aluno} Aluno reprovado!')
    print(f'Nota 1: {nota1}/ Nota 2: {nota2}/ Nota 3: {nota3}/ Nota 4: {nota4}')
    print(20*'-')
    print(f'Média: {media}')'''
'''
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

if idade >= 12 and altura >= 1.2:
    print(f"A entrada de {nome} está liberada")
else:
    print(f"A entrada de {nome} não está liberada") '''
nome = "Caio"
idade = 19

# operador ternário
print(nome, "é maior de idade" if idade >= 18 else "é menor de idade") # condição em uma linha