import random 
import string

def gerar_senha(comprimento=12, incluir_maiusculo=True, incluir_minusculo=True,
                incluir_numeros=True, incluir_caracter=True):
    
    caracteres = ""
    if incluir_maiusculo:
        caracteres += string.ascii_uppercase

    if incluir_minusculo:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracter:
        caracteres += string.punctuation

    if not caracteres:
        return ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Senha: {senha}')
    return senha

    ...

def main():
    print("Gerador de Senhas")
    comprimento = int(input("Digite o comprimento da senha (padrão 12): ") or 12)
    incluir_maiusculo = input("Incluir letras maiúsculas? (s/n, padrão = sim): ").lower() != 'n'
    incluir_minusculo = input("Incluir letras minúsculas? (s/n, padrão = sim): ").lower() != 'n'
    incluir_numeros = input("Incluir números? (s/n, padrão = sim): ").lower() != 'n'
    incluir_caracter = input("Incluir caracteres especiais? (s/n, padrão = sim): ").lower() != 'n'

    senha= gerar_senha(comprimento, incluir_maiusculo, incluir_minusculo,
                        incluir_numeros, incluir_caracter)
    
    print(f'Senha gerada: {senha}')

    with open('aula08/senha.txt', 'a') as s:
        s.write(f'\n{senha}')


if __name__ == "__main__":
    main()