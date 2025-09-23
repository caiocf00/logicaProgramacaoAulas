import json
import os
livros= []
# cadastrar, listar, atualizar e excluir livros, armazenando as informações em arquivos JSON.

while True:
    livro= {}

    
    print('--- SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ---')
    # menu 
    print('1 - Cadastrar livro')
    print('2 - Listar')
    print('3 - Atualizar')
    print('4 - Excluir livro')
    print('Digite ''5'' para encerrar .')

    opcao = input('Digite a opção que deseja selecionar:')
     
    match opcao:
        case '1':
            livro['nome'] = input('Digite o nome do livro: ').strip().lower()
            livro['autor'] = input('Digite o nome do autor do livro: ').strip().lower()
            arquivo = input('Digite o nome do arquivo: ')
            livros.append(livro)
            
            with open(fr"{arquivo}", "w", encoding='utf-8') as f:
             json.dump(livro, f,ensure_ascii=False, indent=4)
             print('livro cadstrado com sucesso.')
        case '2':
           for livro in livros:
              print(f"Nome: {livro['nome']} , Autor: {livro['autor']}")
           arquivo = input('Digite o nome do arquivo: ')
           with open(fr"{arquivo}", "r", encoding='utf-8') as f:
                arquivo = json.load(f)
                print(f"Nome: {livro['nome']} , Autor: {livro['autor']}")            
        case '3':
          ...
        case '4':
         delete = input('Digite o nome do livro que deseja excluir: ').strip().lower()
         with open("biblioteca", "w", encoding="utf-8") as f: 
          excluir = json.load(f) 
          for livro in excluir:
            if livro['nome'] == delete:
                excluir.remove(livro)
                with open("biblioteca", "r", encoding="utf-8") as f:
                    json.dump(excluir, f, ensure_ascii=False, indent=4)
                print(f'Livro {delete} excluído com sucesso!')
        case '5':
          print('Fim do programa.')
          break