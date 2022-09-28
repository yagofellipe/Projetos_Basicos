#Recebendo o valor 
conta = float(input('Qual o valor da conta? '))
desejo = str(input('Deseja adicionar gorjeta? S ou N: '))
#Adicionando gorjeta
if desejo == 'S' or desejo == 's':
    gorjeta = float(input('Qual a gorgeta em porcentagem? (ex: 10): '))/100
    print('O valor da sua conta é {}'.format(conta*(1+gorjeta)))
else:
    print(f'O valor final da conta é: {conta}')

