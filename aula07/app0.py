
'''
Crie uma aplicação de banco, onde o usuário se cadastra e cria uma conta corrente que começa com 0 de saldo.O usuário terá as opções: Criar conta, exibir dados da conta, depositar valor, 
sacar valor, encerrar a conta, sair do programa (Usando funções).
'''

import os 
import json 
limpar = os.system("cls")   
saldo = 0
nome = ""
conta_ativa = False

usuario = {}
def criar_conta():
    global nome, conta_ativa
    nome = input('Digite o nome do usuário: ').strip()
    conta_ativa = True
    print(f"Conta criada com sucesso para {nome}!")
    print(f"Saldo inicial: R$ {saldo:.2f}")
    with open(fr"conta.json", "w", encoding='utf-8') as f:
        json.dump(nome, f,ensure_ascii=False, indent=4)

def exibir_dados():
    if conta_ativa:
        with open(fr"conta.json", "r", encoding='utf-8') as f:
            dados = json.load(f)
            print(f"Nome do usuário: {dados}")
    else:
        print("Nenhuma conta ativa. Por favor, crie uma conta primeiro.")

def depositar_valor():
    global saldo
    if conta_ativa:
        valor = float(input("Digite o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor inválido. O depósito deve ser maior que R$ 0,00.")
    else:
        print("Nenhuma conta ativa. Por favor, crie uma conta primeiro.")

def sacar_valor():
    global saldo
    if conta_ativa:
        valor = float(input("Digite o valor a ser sacado: R$ "))
        if 0 < valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor inválido. O saque deve ser maior que R$ 0,00.")
    else:
        print("Nenhuma conta ativa. Por favor, crie uma conta primeiro.")

def encerrar_conta():
    global nome, saldo, conta_ativa
    if conta_ativa:
        if saldo == 0:
            with open(fr"conta.json", "w", encoding='utf-8') as f:
                f.write("")
            print(f"Conta de {nome} encerrada com sucesso.")
            conta_ativa = False
        else:
            print("Para encerrar a conta, o saldo deve ser R$ 0,00. Por favor, saque ou deposite o valor necessário.")
    else:
        print("Nenhuma conta ativa para encerrar.") 

limpar 

def menu():
    print("\n=== Menu do Banco ===")
    print("1. Criar conta")
    print("2. Exibir dados da conta")
    print("3. Depositar valor")
    print("4. Sacar valor")
    print("5. Encerrar conta")
    print("6. Sair do programa")
    escolha = input("Escolha uma opção (1-6): ")
    return escolha

while True:
    escolha = menu()
    match escolha:
        case '1':
            criar_conta()
        case '2':
            exibir_dados()
        case '3':
            depositar_valor()
        case '4':
            sacar_valor()
        case '5':
            encerrar_conta()
        case '6':
            print("Saindo do programa. Até a próxima!")
            break