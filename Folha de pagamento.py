def menu():
    print(f'-' * 50)
    print('Bem vindo ao sistema de folha de pagamento da Marketing é Tudo!')
    print(f'-' * 50)
    print('Digite o número da opção desejada:')
    print(f'-' * 50)
    print('1 - INSERIR FUNCIONÁRIO;')
    print('2 - REMOVER FUNCIONÁRIO;')
    print('3 - FOLHA DE PAGAMENTO DE UM FUNCIONÁRIO;')
    print('4 - RELATÓRIO DE TODOS OS FUNCIONÁRIOS;')
    print('5 - MOSTRAR FUNCIONÁRIO COM MAIOR SALÁRIO ;')
    print('6 - MOSTRAR O FUNCIONÁRIO COM MAIS FALTAS;')
    print('OUTRO NÚMERO PARA FINALIZAR O PROGRAMA.')
    print(f'-' * 50)
    print()

    resp = int(input())
    if resp == 1:
        inserir()
    elif resp == 2:
        remover()
    elif resp == 3:
        folha_de_pag()
    elif resp == 4:
        relatorio()
    elif resp == 5:
        maiorsal()
    elif resp == 6:
        maisfaltas()


def inserir():
    print('')
    print('1 - INSERIR FUNCIONÁRIO')
    print('-' * 50)
    
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
        sal_fixo = 1500
        vol_vendas = float(input('Digite o valor do volume de vendas do funcionário: '))
        sal_bruto = sal_fixo + (vol_vendas * 0.09)
    else:
        sal_fixo = float(input('Digite o salário do funcionário: '))
        while sal_fixo < 2150 or sal_fixo > 6950:
            print('Valor inválido. Tente novamente.')
            sal_fixo = float(input('Digite o salário do funcionário: '))
    
    desc_faltas = ((sal_fixo/30)* num_falta)
    
    sal_bruto = sal_bruto - desc_faltas
    
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
    funcionarios[matricula] = [nome.title(), cod_func, num_falta, desc_faltas, sal_bruto, imposto, sal_liq]
    print('')
    print('FUNCIONÁRIO INSERIDO.')
    print('')

    frase = 'inserir mais algum funcionário'
    func = 1
    voltar(frase, func)

def remover():
    print('')
    print('2 - REMOVER FUNCIONÁRIO')
    print('-' * 50)
    print('MATRÍCULAS DISPONÍVEIS PARA REMOÇÃO: ')
    for num, nome in funcionarios.items():
        print(f'{nome[0]}: {num}')
    print('-' * 50)
    matricula = int(input('Digite o número da matrícula do funcionário que deseja remover: '))
    if matricula in funcionarios.keys():
        print(funcionarios[matricula][0])
        nome = input('Para confirmar, digite o primeiro nome do funcionário: ')
        if nome.title() == funcionarios[matricula][0]:
            func_remov = funcionarios.pop(matricula)
            print(f'O FUNCIONÁRIO {func_remov[0].upper()} FOI REMOVIDO.')
        else:
            print('-' * 50)    
            print('O nome do funcionário foi digitado incorretamente.')
            remover()
    else:
        print("Esse funcionário não existe.")
        remover()
    print('')
    
    frase = 'remover mais algum funcionário'
    func = 2
    voltar(frase, func)

def folha_de_pag():
    print('')
    print('3 - FOLHA DE PAGAMENTO')
    print('-' * 50)
    print('MATRÍCULAS DISPONÍVEIS PARA APRESENTAÇÃO: ')
    for num, nome in funcionarios.items():
        print(f'{nome[0]}: {num}')
    print('-' * 50)
    matricula = int(input('Digite o número de matrícula do funcionário: '))
    while matricula not in funcionarios.keys():
        print('Número de matrícula inválido.')
        matricula = int(input('Digite o número de matrícula do funcionário: '))
        
    if matricula in funcionarios.keys():
        print('-'*50)
        print(f'Número de matrícula:   {matricula}')
        print(f'Nome do funcionário:   {funcionarios[matricula][0]}')
        print(f'Código do funcionário: {funcionarios[matricula][1]}')
        print(f'Número de faltas:      {funcionarios[matricula][2]}')
        print(f'Desconto das faltas:   {funcionarios[matricula][3]}')
        print(f'Salário bruto:         {funcionarios[matricula][4]}')
        print(f'Imposto:               {funcionarios[matricula][5]}%')
        print(f'Salário líquido:       {funcionarios[matricula][6]}')
        print('')

    frase = 'mostrar a folha de pagamento de mais algum funcionário'
    func = 3
    voltar(frase, func)

def relatorio():
    print('')
    print('4 - RELATÓRIO GERAL')
    print('-' * 50)
    for matricula, lista in funcionarios.items():
        print(f'Número de Matrícula: {matricula}')
        print(f'Nome: {lista[0]}')
        print(f'Códigoda função: {lista[1]}')
        print(f'Salário bruto: {lista[4]}')
        print(f'Salário líquido: {lista[6]}')
        print('')

    frase = 'realizar o relatório novamente'
    func = 4
    voltar(frase, func)

def maiorsal():
    maior_s = 0
    for i in funcionarios.keys():
        if funcionarios[i][6] > maior_s:
            maior_s = funcionarios[i][6]
            matricula = funcionarios[i]
    print('MAIOR SALÁRIO:')
    print(f'Número de matrícula: {matricula}')
    print(f'Nome do funcionário: {matricula[0]}')
    print(f'Código do funcionário: {matricula[1]}')
    print(f'Salário bruto: {matricula[4]}')
    print(f'Imposto: {matricula[5]}%')
    print(f'Salário líquido: {matricula[6]}')
    
    frase = 'mostrar o funcionário com maior salário novamente'
    func = 5
    voltar(frase, func)

def maisfaltas():
    mais_f = 0
    for i in funcionarios.keys():
        if funcionarios[i][2] > mais_f:
            mais_f = funcionarios[i][2]
            matricula = funcionarios[i]
    print('MAIOR NÚMERO DE FALTAS:')     
    print(f'Número de matrícula: {matricula}')
    print(f'Nome do funcionário: {matricula[0]}')
    print(f'Código do funcionário: {matricula[1]}')
    print(f'Número de faltas: {matricula[2]}')
    print(f'Desconto das faltas: {matricula[3]}')
    
    frase = 'mostrar o funcionário com maior número de faltas novamente'
    func = 6
    voltar(frase, func)

def voltar(frase, func):
    print(f'Digite 1 se você deseja {frase};')
    print('Digite 2 se você deseja voltar ao menu;')
    print('Digite outro número se você deseja finalizar o programa.')
    resp = int(input())
    while resp != 1 and resp != 2:
        print(f'Digite 1 se você deseja {frase} algum funcionário;')
        print('Digite 2 se você deseja voltar ao menu;')
        print('Digite outro número se você deseja finalizar o programa.')
        resp = int(input())
    if resp == 1:
        if func == 1:
            inserir()
        elif func == 2:
            remover()
        elif func == 3:
            folha_de_pag()
        elif func == 4:
            relatorio()
    elif resp == 2:
        menu()

funcionarios = {1: ['João', 101, 0, 0, 1000.00, 0, 1591.00], 39: ['Jorge', 101, 0, 0, 1000.00, 0, 1590.00]}
menu() 
print('Obrigado por acessar o programa!')
