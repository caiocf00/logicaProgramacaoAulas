#impotação
import json
try:
    arquivo= input('Digitr o nome do arquivo:').strip().lower()

    with open(f'{arquivo}.json', 'r', encoding="utf-8")as f:
        dados= json.load(f)

    print(f'{'-'*20}DADOS {'-'*20}\n')
    for dado in dados:
            for chave in dado:
                print(f'{chave.captalize()} : {dado.get(chave)}')
            print('-'*40)
except Exception as e:
     print(f'Não foi possível ler o arquivo. {e}')
