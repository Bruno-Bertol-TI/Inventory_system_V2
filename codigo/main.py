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
inventario_produtos = []

def main():

    while True:

        exibir_servicos()

        escolher_servico = int(input('| Escolha qual função deseja executar agora: '))

        os.system('cls')
        if escolher_servico in menu_servicos:
            if escolher_servico == 1:
                adicionar_produto()
            elif escolher_servico == 2:
                remover_produto()
            elif escolher_servico == 3:
                listar_produto()
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

def pressione_enter():
    press = input('| Pressione o [ENTER] para continuar trabalhando. |')
    os.system('cls')

def exibir_servicos():
    for numero, servico in enumerate(menu_servicos):
        print(f'| {numero + 1} | {menu_servicos[servico]}')

def anular_duplicidade_produtos(cad_nome_pdt, cad_qtd_pdt, cad_preco_pdt):

    if cad_nome_pdt not in estoque_produtos_teste_duplicidade:
        estoque_produtos_teste_duplicidade.add(cad_nome_pdt)
        inventario_produtos.append({'nome_produto': cad_nome_pdt, 'quantidade_produto': cad_qtd_pdt, 'valor_produto': cad_preco_pdt})
        print(f'| {linha_divisao} |\n| Produto cadastrado com sucesso... |\n| {linha_divisao} |')
        print(f'| O produto: {cad_nome_pdt} contém: {cad_qtd_pdt} unidades, e custa: R$ {cad_preco_pdt} \n| {linha_divisao} |')
    else:
        os.system('cls')
        print('| Este produto ja foi cadastrado na lista... |')
        # exibir produtos.

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
    os.system('cls')

    anular_duplicidade_produtos(cadastro_nome_produto, cadastro_quantidade_produto, cadastro_preco_produto)
    pressione_enter()

def remover_produto():

    listar_produto()
    
    id_remover = input('| Digite o ID do item que deseja remover: ')
    if id_remover.isdigit():
        id_remover = int(id_remover)
        if id_remover >= 0 and id_remover <= len(inventario_produtos):
            del inventario_produtos[id_remover]
            os.system('cls')
            print('| Produto removido com sucesso...')
            print(linha_divisao)
            return listar_produto()
        else:
            print('| Este ID ja foi removido antes ou nunca existiu...')
            pressione_enter()
            return remover_produto()

def listar_produto():

    print(linha_divisao)
    print('| Lista de produtos...')
    print(linha_divisao)
    if not inventario_produtos:
        print('| A lista esta vazia...')
        print(linha_divisao )
    else:
        for i, produto_info in enumerate(inventario_produtos):
            produto = produto_info['nome_produto']
            quantidade = produto_info['quantidade_produto']
            valor = produto_info['valor_produto']
            print(f'| ID: {i} | Produto: {produto} | Quantidade: {quantidade} | Valor: {valor} |')
            print(linha_divisao)
    
    pressione_enter()

def encerrar_sistema():
    exit()

main()