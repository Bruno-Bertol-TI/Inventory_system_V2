import os

linha_divisao = 60 * '-'

menu_servicos = {
    1: 'adicionar_produto',
    2: 'remover_produto',
    3: 'listar_produto',
    4: 'buscar_produto',
    5: 'ajustar_quantidade',
    6: 'encerrar_programa'
}

estoque_produtos_teste_duplicidade = set()
armazenamento_dados_produtos = []

def pressione_enter():
    press = input('| Pressione o [ENTER] para continuar trabalhando. |')

def exibir_servicos():
    for numero, servico in enumerate(menu_servicos):
        print(f'| {numero + 1} | {menu_servicos[servico]}')

def anular_duplicidade_produtos(cad_nome_pdt, cad_qtd_pdt, cad_preco_pdt):

    if cad_nome_pdt not in estoque_produtos_teste_duplicidade:
        estoque_produtos_teste_duplicidade.add(cad_nome_pdt)
        armazenamento_dados_produtos.append({'cad_nome_pdt': {'quantidade_produto': cad_qtd_pdt, 'valor_produto': cad_preco_pdt}})
        print(f'| {linha_divisao} |\n| Produto cadastrado com sucesso... |\n| {linha_divisao} |')
        print(f'| O produto: {cad_nome_pdt} contém: {cad_qtd_pdt} unidades, e custa: R$ {cad_preco_pdt} \n| {linha_divisao} |')
    else:
        os.system('cls')
        print('| Este produto ja foi cadastrado na lista... |')

def adicionar_produto():

    print(f'| Adicionar Produto ao Estoque |\n| {linha_divisao} |')

    print('| Exemplo: Patinete Elétrico |')
    cadastro_nome_produto = input('| Descreva qual o nome do produto: ').lower()
    print(f'| {linha_divisao} |')
    print('| Exemplo: 500 |')
    cadastro_quantidade_produto = int(input('| Descreva a quantidade do produto: '))
    print(f'| {linha_divisao} |')
    print('| Exemplo: 12.30 |')
    cadastro_preco_produto = float(input('| Descreva o valor do produto: '))

    anular_duplicidade_produtos(cadastro_nome_produto, cadastro_quantidade_produto, cadastro_preco_produto)
    pressione_enter()

def encerrar_sistema():
    exit()

while True:

    exibir_servicos()

    escolher_servico = int(input('| Escolha qual função deseja executar agora: '))

    os.system('cls')
    if escolher_servico in menu_servicos:
        if escolher_servico == 1:
            adicionar_produto()
        elif escolher_servico == 2:
            ...
        elif escolher_servico == 3:
            ...
        elif escolher_servico == 4:
            ...
        elif escolher_servico == 5:
            ...
        elif escolher_servico == 6:
            encerrar_sistema()
        else:
            os.system('cls')
            print('SISTEMA CORROMPIDO, CHAMAR ASSISTENCIA (SUPORTE TI)')
            break
    else:
        os.system('cls')
        print(f'| Ops, a opção {escolher_servico} é invalida por enquanto \n| tente novamente uma opcao valida...')