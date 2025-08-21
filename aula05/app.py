'''while True:
    try:
        #entrada de dados
        etanol= float(input('Digite o valor do etanol:').replace(',','.'))
        gasolina = float(input("Digite o valor da gasolina:").replace(',','.'))
        calculo = (etanol/gasolina)*100
        resultado = 'gasolina' if calculo > 70 else 'Etanol'

        print(f'Resultado = {calculo:.2f}%. Compensa abastecer com {resultado}.')

        opcao = input('Deseja refazer o calculo?(s/n)').lower().strip()
        match opcao:
            case 's':
                continue
            case'n':
                break
            case _:
                print(f'Opção Invalida')
                continue
    except Exception as e:
        print(f'Não foi possivel executar a operação.')
    continue'''