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
'''
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
'''
'''
# Lista de salas com filmes e suas classificações
salas = {
    1: {"filme": "Divertida Mente 2", "idade_minima": 0},
    2: {"filme": "Deadpool & Wolverine", "idade_minima": 16},
    3: {"filme": "Annabelle", "idade_minima": 18},
    4: {"filme": "Homem-Aranha: Sem Volta Para Casa", "idade_minima": 12},
    5: {"filme": "Minions 2", "idade_minima": 0}
}

print("Bem-vindo ao cinema!\n")

# Usuário informa a idade
idade = int(input("Digite sua idade: "))

while True:
    print("\n--- Lista de Filmes ---")
    for sala, info in salas.items():
        print(f"Sala {sala} - {info['filme']} (Classificação: {info['idade_minima']} anos)")

    escolha = int(input("\nDigite o número da sala que deseja assistir: "))

    # Verifica se a sala existe
    if escolha in salas:
        filme = salas[escolha]["filme"]
        idade_min = salas[escolha]["idade_minima"]

        if idade >= idade_min:
            print(f"\n✅ Ingresso gerado! Bom filme: {filme} 🎬")
            break
        else:
            print(f"\n❌ Você não tem idade para assistir {filme}. Escolha outro filme.")
    else:
        print("\nSala inválida. Tente novamente.")'''
'''
print("Bem-vindo ao cinema!\n")

# Usuário informa a idade
idade = int(input("Digite sua idade: "))

while True:
    print("\n--- Lista de Filmes ---")
    print("1 - Divertida Mente 2 (Livre)")
    print("2 - Deadpool & Wolverine (16 anos)")
    print("3 - Annabelle (18 anos)")
    print("4 - Homem-Aranha: Sem Volta Para Casa (12 anos)")
    print("5 - Minions 2 (Livre)")

    escolha = int(input("\nDigite o número da sala que deseja assistir: "))

    if escolha == 1:
        if idade >= 0:
            print("✅ Ingresso gerado! Bom filme: Divertida Mente 2 🎬")
            break
        else:
            print("❌ Você não tem idade para esse filme.")

    elif escolha == 2:
        if idade >= 16:
            print("✅ Ingresso gerado! Bom filme: Deadpool & Wolverine 🎬")
            break
        else:
            print("❌ Você não tem idade para esse filme.")

    elif escolha == 3:
        if idade >= 18:
            print("✅ Ingresso gerado! Bom filme: Annabelle 🎬")
            break
        else:
            print("❌ Você não tem idade para esse filme.")

    elif escolha == 4:
        if idade >= 12:
            print("✅ Ingresso gerado! Bom filme: Homem-Aranha 🎬")
            break
        else:
            print("❌ Você não tem idade para esse filme.")

    elif escolha == 5:
        if idade >= 0:
            print("✅ Ingresso gerado! Bom filme: Minions 2 🎬")
            break
        else:
            print("❌ Você não tem idade para esse filme.")

    else:
        print("Opção inválida, tente novamente.")'''