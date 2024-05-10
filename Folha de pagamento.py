def menu():
    print('-' * 50)
    print('Bem vindo ao sistema de folha de pagamento da Marketing é Tudo!')
    print('Para utilizar todas as funcionalidades é necessário acessar pelo menu abaixo:')
    print('Digite 1 para inserir um funcionário;')
    print('Digite 2 para remover um funcionário;')
    print('Digite 10 para finalizar o programa.')

    resp = int(input())
    if resp == 1:
        inserir()
    elif resp == 2:
        remover()
    elif resp == 10:
        print('Obrigado por acessar o programa!')

def inserir():
    matricula = int(input('Digite o número de matrícula: '))
    if matricula in funcionarios.keys():
        print('Matrícula já existente. Insira outro número.')
        inserir()

    nome = input('Digite o nome do funcionário: ')

    cod_func = int(input('Digite o código da função do funcionário: '))
    while cod_func != 101 and cod_func != 102:
        print('O código inserido é invalido. Tente novamente.')
        cod_func = int(input('Digite o código da função do funcionário: '))

    num_falta = int(input('Digite a quantidade de faltas do funcionário no mês: '))
    while num_falta > 30:
        print('Número de faltas excedeu o máximo permitido. Tente novamente.')
        num_falta = int(input('Digite a quantidade de faltas do funcionário no mês: '))

    if cod_func == 101:
        sal_bruto = 1500
        vol_vendas = float(input('Digite o valor do volume de vendas do funcionário: '))
        sal_bruto = sal_bruto + (vol_vendas * 0.09)
    else:
        sal_bruto = float(input('Digite o salário do funcionário: '))
        while sal_bruto < 2150 or sal_bruto > 6950:
            print('Valor inválido. Tente novamente.')
            sal_bruto = float(input('Digite o salário do funcionário: '))
    
    sal_bruto = sal_bruto - (sal_bruto/30 * num_falta)

    if sal_bruto <= 2259.20:
        sal_liq = sal_bruto
    elif 2259.20 < sal_bruto <= 2828.65:
        sal_liq = sal_bruto - (sal_bruto * 0.075)
    elif 2828.65 < sal_bruto <= 3751.05:
        sal_liq = sal_bruto - (sal_bruto * 0.15)
    elif 3751.05 < sal_bruto <= 4664.68:
        sal_liq = sal_bruto - (sal_bruto * 0.225)
    elif 4664.68 < sal_bruto:
        sal_liq = sal_bruto - (sal_bruto * 0.275)

    funcionarios[matricula] = [nome, cod_func, num_falta, sal_bruto, sal_liq]

    print('-' * 50)
    print('Digite 1 se você deseja inserir mais algum funcionário;')
    print('Digite 2 se você deseja voltar ao menu;')
    print('Digite 3 se você deseja finalizar o programa.')
    resp = int(input())
    while resp < 1 or resp > 3:
        print('-' * 50)
        print('Digite 1 se você deseja inserir mais algum funcionário;')
        print('Digite 2 se você deseja voltar ao menu;')
        print('Digite 3 se você deseja finalizar o programa.')
        resp = int(input())
    if resp == 1:
        inserir()
    elif resp == 2:
        menu()

def remover():
    matricula = int(input('Digite o número da matrícula do funcionário que deseja remover: '))
    if matricula in funcionarios.keys():
        print(funcionarios[matricula][0])
        nome = input('Para confirmar, digite o nome do funcionário completo: ')
        if nome in funcionarios[matricula][0]:
            func_remov = funcionarios.pop(matricula)
            print(f'O funcionário {func_remov[0]} foi removido do sistema.')
        else:
            print('O nome do funcionário foi digitado incorretamente.')
            remover()
    else:
        print("Esse funcionário não existe.")
        remover()

funcionarios = {}
menu()