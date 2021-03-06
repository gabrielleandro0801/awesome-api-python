import requests
import json

print('##########################')
print('### Consulta de Moedas ###')
print('##########################')

def main():
    print('\nEscolha a Moeda:')
    print('<1> Dolar Comercial')
    print('<2> Dolar Turismo')
    print('<3> Euro')
    print('Sua opcao: ')
    opcao = int(input())

    if opcao == 1:
        request = requests.get('https://economia.awesomeapi.com.br/USD-BRL/')
    elif opcao == 2:
        request = requests.get('https://economia.awesomeapi.com.br/USDT-BRL/')
    elif opcao == 3:
        request = requests.get('https://economia.awesomeapi.com.br/EUR-BRL/')
    else:
        print('Opcao invalida!')
        exit()

    money_data = json.loads(request.text)

    if 'status' not in money_data:
        print('Dados do(a) ' + money_data[0]['name'])
        print('Valor atual: R$ {:.2f}' .format(float(money_data[0]['bid'])))

    opcao = input('\nDeseja buscar novamente? ')

    if opcao.lower() == 'sim':
        main()
    else:
        print('Fim de Programa')


if __name__ == '__main__':
    main()
