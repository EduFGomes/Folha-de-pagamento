def menu():
    print('')
    print('Digite o número da opção desejada:')
    print('-' * 50)
    print('1 - INSERIR FUNCIONÁRIO;')
    print('2 - REMOVER FUNCIONÁRIO;')
    print('3 - FOLHA DE PAGAMENTO DE UM FUNCIONÁRIO;')
    print('4 - RELATÓRIO DE TODOS OS FUNCIONÁRIOS;')
    print('5 - MOSTRAR FUNCIONÁRIO COM MAIOR SALÁRIO;')
    print('6 - MOSTRAR O FUNCIONÁRIO COM MAIS FALTAS;')
    print('OUTRO NÚMERO PARA FINALIZAR O PROGRAMA.')
    print('-' * 50)

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
    while matricula < 0:
        print('Matrícula não pode ser negativa. Insira outro número.')
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
        sal_fixo = sal_fixo + (vol_vendas * 0.09)
    else:
        sal_fixo = float(input('Digite o salário do funcionário: '))
        while sal_fixo < 2150 or sal_fixo > 6950:
            print('Valor inválido. Tente novamente.')
            sal_fixo = float(input('Digite o salário do funcionário: '))
    
    desc_faltas = ((sal_fixo/30)* num_falta)
    
    sal_bruto = sal_fixo - desc_faltas
    
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

    frase = 'INSERIR FUNCIONÁRIO NOVAMENTE'
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
        print('')
        print(f'FUNCIONÁRIO SELECIONADO: {funcionarios[matricula][0]}')
        print('')
        nome = input('Para confirmar, digite o primeiro nome do funcionário: ')
        if nome.title() in funcionarios[matricula][0]:
            func_remov = funcionarios.pop(matricula)
            print('')
            print(f'O FUNCIONÁRIO {func_remov[0].upper()} FOI REMOVIDO.')
        else:
            print('')
            print('O nome do funcionário foi digitado incorretamente.')
            remover()
    else:
        print('')
        print("Esse funcionário não existe.")
        remover()
    print('')
    
    frase = 'REMOVER FUNCIONÁRIO NOVAMENTE'
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

    frase = 'FOLHA DE PAGAMENTO NOVAMENTE'
    func = 3
    voltar(frase, func)

def relatorio():
    print('')
    print('4 - RELATÓRIO GERAL')
    print('-' * 50)
    for matricula, lista in funcionarios.items():
        print(f'Número de Matrícula: {matricula}')
        print(f'Nome:                {lista[0]}')
        print(f'Códigoda função:     {lista[1]}')
        print(f'Salário bruto:       {lista[4]}')
        print(f'Salário líquido:     {lista[6]}')
        print('')

    frase = 'RELATÓRIO GERAL NOVAMENTE'
    func = 4
    voltar(frase, func)

def maiorsal():
    listaMS = {}
    maior_s = 0
    for i in funcionarios.keys():
        aux = funcionarios[i]
        if aux[6] > maior_s:
            listaMS = {}
            listaMS[i] = [aux[0], aux[1], aux[4], aux[5], aux[6]]
            maior_s = aux[6]
        elif aux[6] == maior_s:
            listaMS[i] = [aux[0],aux[1], aux[4], aux[5], aux[6]]
    print('MAIOR SALÁRIO:')
    for matricula, lista in listaMS.items():
        print(f'-'*50)
        print(f'Número de matrícula:   {matricula}')
        print(f'Nome do funcionário:   {lista[0]}')
        print(f'Código do funcionário: {lista[1]}')
        print(f'Salário bruto:         {lista[2]}')
        print(f'Imposto:               {lista[3]}%')
        print(f'Salário líquido:       {lista[4]}')
    print('')

    frase = 'MAIOR SALÁRIO NOVAMENTE'
    func = 5
    voltar(frase, func)

def maisfaltas():
    listaMF = {}
    mais_f = 0
    for i in funcionarios.keys():
        aux = funcionarios[i]
        if aux[2] > mais_f:
            listaMF = {}
            listaMF[i] = [aux[0], aux[1], aux[2], aux[3]]
            mais_f = funcionarios[i][2]
        elif aux[2] == mais_f:
            listaMF[i] = [aux[0], aux[1], aux[2], aux[3]]
    print('MAIOR NÚMERO DE FALTAS:')
    for matricula, lista in listaMF.items():
        print('-'*50)
        print(f'Número de matrícula:   {matricula}')
        print(f'Nome do funcionário:   {lista[0]}')
        print(f'Código do funcionário: {lista[1]}')
        print(f'Número de faltas:      {lista[2]}')
        print(f'Desconto das faltas:   {lista[3]}')
    print('')
    
    frase = 'MAIOR NÚMERO DE FALTAS NOVAMENTE'
    func = 6
    voltar(frase, func)

def voltar(frase, func):
    print(f'1 - {frase};')
    print('2 - VOLTAR AO MENU;')
    print('OUTRO NÚMERO PARA FINALIZAR O PROGRAMA.')
    print('-'*50)
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
        elif func == 5:
            maiorsal()
        elif func == 6:
            maisfaltas()
    elif resp == 2:
        menu()

funcionarios = {1: ['João Pedro', 101, 0, 0, 1590.00, 0, 1590.00], 2: ['Jorge', 101, 1, 50, 1540.00, 0, 1540.00]}
print('Bem vindo ao sistema de folha de pagamento da Marketing é Tudo!')
menu() 
print('')
print('Obrigado por acessar o programa!')
