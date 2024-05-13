def menu():
    print('-' * 50)
    print('Bem vindo ao sistema de folha de pagamento da Marketing é Tudo!')
    print('Para utilizar todas as funcionalidades é necessário acessar pelo menu abaixo:')
    print('Digite 1 para inserir um funcionário;')
    print('Digite 2 para remover um funcionário;')
    print('Digite 3 para mostrar a folha de pagamento de um funcionário;')
    print('Digite 10 para finalizar o programa.')

    resp = int(input())
    if resp == 1:
        inserir()
    elif resp == 2:
        remover()
    elif resp == 3:
        folha_de_pag()
    elif resp == 10:
        print('Obrigado por acessar o programa!')

def inserir():
    matricula = int(input('Digite o número de matrícula: '))
    while matricula in funcionarios.keys():
        print('Matrícula já existente. Insira outro número.')
        matricula = int(input('Digite o número de matrícula: '))
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
        imposto = 0
    elif 2259.20 < sal_bruto <= 2828.65:
        sal_liq = sal_bruto - (sal_bruto * 0.075)
        imposto = 7.5
    elif 2828.65 < sal_bruto <= 3751.05:
        sal_liq = sal_bruto - (sal_bruto * 0.15)
        imposto = 15
    elif 3751.05 < sal_bruto <= 4664.68:
        sal_liq = sal_bruto - (sal_bruto * 0.225)
        imposto = 22.5
    elif 4664.68 < sal_bruto:
        sal_liq = sal_bruto - (sal_bruto * 0.275)
        imposto = 27.5
    funcionarios[matricula] = [nome.title(), cod_func, num_falta, sal_bruto, imposto, sal_liq]

    resp = 'inserir mais'
    func = 1
    voltar(resp, func)

def remover():
    matricula = int(input('Digite o número da matrícula do funcionário que deseja remover: '))
    if matricula in funcionarios.keys():
        print(funcionarios[matricula][0])
        nome = input('Para confirmar, digite o nome do funcionário completo: ')
        if nome.title() in funcionarios[matricula][0]:
            func_remov = funcionarios.pop(matricula)
            print(f'O funcionário {func_remov[0]} foi removido do sistema.')
        else:
            print('O nome do funcionário foi digitado incorretamente.')
            remover()
    else:
        print("Esse funcionário não existe.")
        remover()
    
    resp = 'remover mais'
    func = 2
    voltar(resp, func)

def folha_de_pag():
    matricula = int(input('Digite o número de matrícula do funcionário: '))
    while matricula not in funcionarios.keys():
        print('Número de matrícula inválido.')
        matricula = int(input('Digite o número de matrícula do funcionário: '))
        
    if matricula in funcionarios.keys():
        print('-'*50)
        print(f'Número de matrícula: {matricula}')
        print(f'Nome do funcionário: {funcionarios[matricula][0]}')
        print(f'Código do funcionário: {funcionarios[matricula][1]}')
        print(f'Número de faltas: {funcionarios[matricula][2]}')
        print(f'Salário bruto: {funcionarios[matricula][3]}')
        print(f'Imposto: {funcionarios[matricula][4]}%')
        print(f'Salário líquido: {funcionarios[matricula][5]}')
        print('-'*50)

        resp = 'mostrar a folha de pagamento de mais'
        func = 3
        voltar(resp, func)

def voltar(resp, func):
    print('-' * 50)
    print(f'Digite 1 se você deseja {resp} algum funcionário;')
    print('Digite 2 se você deseja voltar ao menu;')
    print('Digite 3 se você deseja finalizar o programa.')
    resp = int(input())
    while resp < 1 or resp > 3:
        print('-' * 50)
        print(f'Digite 1 se você deseja {resp} algum funcionário;')
        print('Digite 2 se você deseja voltar ao menu;')
        print('Digite 3 se você deseja finalizar o programa.')
        resp = int(input())
    if resp == 1:
        if func == 1:
            inserir()
        elif func == 2:
            remover()
        elif func == 3:
            folha_de_pag()
    elif resp == 2:
        menu()

funcionarios = {}
menu() 
