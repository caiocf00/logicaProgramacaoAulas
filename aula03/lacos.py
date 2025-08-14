'''crie um sistema que calcule o indice de massa corporal (IMC) de uma pessoa, mostre o valor do IMC na tela e se o usuario precisa emagrecer ou engordar, utilize a tabela do imc para definir os valores
Classificação do IMC
Faixa de IMC (kg/m²)
Abaixo do peso
Menos de 18,5
Peso normal
18,5 a 24,9
Sobrepeso
25 a 29,9
Obesidade grau I
30 a 34,9
Obesidade grau II
35 a 39,9
Obesidade grau III
40 ou mais  imc = peso / (altura ** 2)'''

'''altura = float(input("Digite sua altura em metros: ").replace(",","."))

peso = float(input("Digite seu peso em kg: ").replace(",","."))

imc = peso / (altura * altura)

print()
print(f'Seu IMC é: {imc:.2f}')

if imc <= 18.5:
    print('Abaixo do normal')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso') 
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')   
'''

'''problema 2: Um elevador de carga tem capacidade para 200kg. Crie um programa que receba do usuario seu peso e o peso da carga e verifica se a carga está autorizada a usar o elevador ou não.'''
'''peso_usuario = float(input("Digite seu peso em kg: ").replace(",","."))
peso_carga = float(input("Digite o peso da carga em kg: ").replace(',','.'))
peso_total = peso_usuario + peso_carga
print(f'O peso total é: {peso_total} kg')
if peso_total <= 200:
    print('Carga autorizada')
else:
    print('Carga não autorizada, excede o limite de 200kg')'''
'''
#loop 
numero = 10
while numero >= 0
    print(numero)
    numero -= 1'''

'''
'''             

'''while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    
    if idade.isdigit() and int(idade) >= 18:
        print(f"{nome}, você é maior de idade.")
        break
    else:
        print(f"{nome}, você é menor de idade. Tente novamente.")
altura = float(input("Digite sua altura em metros: ").replace(",","."))

peso = float(input("Digite seu peso em kg: ").replace(",","."))

imc = peso / (altura * altura)

print()
print(f'Seu IMC é: {imc:.2f}')

if imc <= 18.5:
    print('Abaixo do normal')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso') 
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')   

opcao = input("Deseja calcular novamente? (s- Sim/n- Não): ").lower()

if opcao == 's':
    continue
else: opcao == 'n'
    print("Saindo do sistema!")
    break'''

print(30*"-",'Cadastro',30*"-")
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu telefone: ")
ano_nascimento = input("Digite seu ano de nascimento: ")

while True:
    print(30*"-","Sistema Console 2 DS",30*"-")
    print("1 - Calcular IMC")
    print('2 - Maioridade' )
    print('3- Calculadora')
    print('4 - Dados pessoais')
    print ('5 - Feliz natal')
    print('6 - Sair')

    opcao = input("Escolha uma opção: ")
    if opcao == '1' :
        altura = float(input('Digite sua altura: ').replace(',','.'))
        peso = float(input('Digite seu peso: ').replace(',','.'))

        imc = peso/(altura * altura)
        print()
        print(f'Seu IMC é: {imc:.2f}')

        if imc <= 18.5:
            print('Abaixo do normal')
        elif imc <= 24.9:
            print('Normal')
        elif imc <= 29.9:
            print('Sobrepeso')
        elif imc <= 34.9:
            print('Obesidade grau I')
        elif imc <= 39.9:
            print('Obesidade grau II')
        else:
            print('Obesidade grau III')
    elif opcao == '2':
        ano_atual = 2025
        idade = ano_atual - ano_nascimento
        print(nome, ' e maior de idade' if idade >= 18 else 'é menor de idade')
    elif opcao == '3':
        print("Calculadora")
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        while True:
            print('1 - Soma')
            print('2 - Divisão')
            print('3 - Subtração')
            print('4 - Multiplicação')
            print('5 - Sair')

            opcao_calculo = input('Escolha uma operação matemática: ')

            if opcao_calculo == '1':
                print(f'Resultado da Soma é: {num1 + num2}')
            elif opcao_calculo == '2':
                print(f'Resultado da Divisão é: {num1/num2}')
            elif opcao_calculo == '3':
                print(f'Resultado da Subtração é: {num1 - num2}')
            elif opcao_calculo == '4':
                print(f'Resultado da Multiplicação é: {num1 * num2}')
            elif opcao_calculo == '5':
                break
            else: 
                print('Opção inválida')
    elif opcao == '4':
        print(30*"-","Dados Pessoais",30*"-")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Telefone: {telefone}")
        print(f"Data de Nascimento: {ano_nascimento}")
    elif opcao == '5':
        linhas = 6
        i = 1

        while i <= linhas:
            espacos = linhas - i
            estrelas = 2 * i - 1
            print(' ' * espacos + '^' * estrelas)
            i += 1
    elif opcao == '6':
        print("Saindo do sistema!")
        break
    else:
        print("Opção inválida!")
