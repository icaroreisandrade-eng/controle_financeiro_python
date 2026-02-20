import pandas as pd
from strings import cabecalho, linha, pausar
from numeros import leiaInt, moeda
menu=['Faturamento total', 'Faturamento por loja', 'Faturamento Loja/Produto',
      'Faturamento e vendas de Cada Produto', 'Sair do Programa']
try:
    tabela=pd.read_excel('Vendas.xlsx')
except FileNotFoundError:
    print(f'Arquivo Vendas.xslx não encontrado')
    exit()
while True:
    cabecalho('Controle Financeiro Empresax')
    cont=1
    for escolha in menu:
        print(f'{cont} - {escolha}')
        cont+=1
    linha()
    opc=leiaInt('Opção: ')
    if opc==1:
        cabecalho('FATURAMENTO TOTAL')
        faturamento_tot = tabela['Valor Final'].sum()
        print(f'{moeda(faturamento_tot).center(50)}')
        pausar()
    elif opc==2:
        cabecalho('FATURAMENTO POR LOJA')
        faturamento_loja=tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum(numeric_only=True).sort_values(by='Valor Final', ascending=False)
        print(faturamento_loja)
        linha()
        pausar()
    elif opc==3:
        cabecalho('FATURAMENTO LOJA/PRODUTO')
        fat_loja_produto=tabela[['ID Loja', 'Produto', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum(numeric_only=True)
        print(fat_loja_produto)
        linha()
        pausar()
    elif opc==4:
        cabecalho('FATURAMENTO E VENDAS DE CADA PRODUTO')
        tot_produtos_vendidos=tabela[['Produto', 'Quantidade', 'Valor Final']].groupby('Produto').sum(numeric_only=True).sort_values(by='Valor Final', ascending=False)
        print(tot_produtos_vendidos)
        linha()
        pausar()
    elif opc==5:
        cabecalho('SAINDO DO PROGRAMA')
        break
    else:
        print('A opção selecionada não existe!')

