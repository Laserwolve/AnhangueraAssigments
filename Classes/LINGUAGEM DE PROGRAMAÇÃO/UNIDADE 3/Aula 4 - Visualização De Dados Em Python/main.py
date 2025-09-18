# -*- coding: utf-8 -*-
"""
Analise de Dados de Vendas de uma Empresa de Varejo
Autor: Andrew
Data: 2025-09-18

Este programa analisa dados de vendas do ultimo ano para identificar padroes
e insights para melhorar o desempenho usando SQLite, Pandas, Matplotlib e Seaborn.
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurar estilo dos graficos
plt.style.use('default')
sns.set_palette("husl")

print("="*60)
print("ANALISE DE DADOS DE VENDAS - EMPRESA DE VAREJO")
print("="*60)

# PASSO 1: CONECTAR AO BANCO DE DADOS SQLite E CRIAR TABELA
print("\n1. CONECTANDO AO BANCO DE DADOS...")

# Passo 1.1: Conectar ao banco de dados (ou criar, se nao existir)
conexao = sqlite3.connect('dados_vendas.db')

# Passo 1.2: Criar um cursor
cursor = conexao.cursor()

# Passo 1.3: Criar uma tabela (se nao existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Limpar tabela se ja existir dados
cursor.execute('DELETE FROM vendas1')

# Passo 1.4: Inserir alguns dados
dados_vendas = [
    ('2023-01-01', 'Produto A', 'Eletronicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletronicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletronicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletronicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletronicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletronicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
]

cursor.executemany('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) 
VALUES (?, ?, ?, ?)
''', dados_vendas)

# Passo 1.5: Confirmar as mudancas
conexao.commit()
print("Banco de dados criado e populado com sucesso!")

# PASSO 2: EXPLORAR E PREPARAR OS DADOS
print("\n2. EXPLORANDO E PREPARANDO OS DADOS...")

# Carregar dados em DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Converter coluna de data para datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Extrair mes e ano da data
df_vendas['mes'] = df_vendas['data_venda'].dt.month
df_vendas['nome_mes'] = df_vendas['data_venda'].dt.strftime('%B')
df_vendas['ano'] = df_vendas['data_venda'].dt.year

print("Dados carregados no DataFrame!")
print(f"Total de vendas: {len(df_vendas)}")
print(f"Periodo analisado: {df_vendas['data_venda'].min().strftime('%d/%m/%Y')} a {df_vendas['data_venda'].max().strftime('%d/%m/%Y')}")

# Exibir informacoes basicas dos dados
print("\n--- INFORMACOES BASICAS DOS DADOS ---")
print(df_vendas.info())
print("\n--- PRIMEIRAS 5 VENDAS ---")
print(df_vendas.head())
print("\n--- ESTATISTICAS DESCRITIVAS ---")
print(df_vendas.describe())

# PASSO 3: ANALISE DOS DADOS
print("\n3. REALIZANDO ANALISES ESPECIFICAS...")

# 3.1 Analise por categoria
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].agg(['sum', 'mean', 'count']).round(2)
vendas_por_categoria.columns = ['Total_Vendas', 'Venda_Media', 'Quantidade_Vendas']

print("\n--- VENDAS POR CATEGORIA ---")
print(vendas_por_categoria)

# 3.2 Analise por mes
vendas_por_mes = df_vendas.groupby(['mes', 'nome_mes'])['valor_venda'].agg(['sum', 'count']).round(2)
vendas_por_mes.columns = ['Total_Vendas', 'Quantidade_Vendas']

print("\n--- VENDAS POR MES ---")
print(vendas_por_mes)

# 3.3 Produto mais vendido por valor
produto_mais_vendido = df_vendas.loc[df_vendas['valor_venda'].idxmax()]
print(f"\n--- PRODUTO COM MAIOR VALOR DE VENDA ---")
print(f"Produto: {produto_mais_vendido['produto']}")
print(f"Categoria: {produto_mais_vendido['categoria']}")
print(f"Valor: R$ {produto_mais_vendido['valor_venda']:,.2f}")
print(f"Data: {produto_mais_vendido['data_venda'].strftime('%d/%m/%Y')}")

# 3.4 Total geral de vendas
total_vendas = df_vendas['valor_venda'].sum()
media_vendas = df_vendas['valor_venda'].mean()

print(f"\n--- RESUMO GERAL ---")
print(f"Total de vendas: R$ {total_vendas:,.2f}")
print(f"Media de vendas: R$ {media_vendas:,.2f}")
print(f"Numero total de transacoes: {len(df_vendas)}")

# PASSO 4: VISUALIZACAO DOS DADOS
print("\n4. GERANDO VISUALIZACOES...")

# Configurar figura com subplots
fig = plt.figure(figsize=(16, 12))
fig.suptitle('ANALISE DE VENDAS - EMPRESA DE VAREJO', fontsize=16, fontweight='bold')

# 4.1 Grafico de barras - Vendas por categoria
plt.subplot(2, 3, 1)
categorias = vendas_por_categoria.index
valores_categoria = vendas_por_categoria['Total_Vendas']
cores = ['#FF6B6B', '#4ECDC4', '#45B7D1']

bars1 = plt.bar(categorias, valores_categoria, color=cores)
plt.title('Vendas Totais por Categoria', fontweight='bold')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=45)

# Adicionar valores nas barras
for bar in bars1:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 50,
             f'R$ {height:,.0f}', ha='center', va='bottom')

# 4.2 Grafico de linha - Evolucao das vendas por mes
plt.subplot(2, 3, 2)
meses = [i for i in range(1, 13) if i in df_vendas['mes'].values]
vendas_mensais = [df_vendas[df_vendas['mes'] == mes]['valor_venda'].sum() for mes in meses]

plt.plot(meses, vendas_mensais, marker='o', linewidth=2, markersize=8, color='#FF6B6B')
plt.title('Evolucao das Vendas Mensais', fontweight='bold')
plt.xlabel('Mes')
plt.ylabel('Valor Total (R$)')
plt.grid(True, alpha=0.3)
plt.xticks(meses)

# 4.3 Grafico de pizza - Distribuicao por categoria
plt.subplot(2, 3, 3)
plt.pie(valores_categoria, labels=categorias, autopct='%1.1f%%', 
        colors=cores, startangle=90)
plt.title('Distribuicao das Vendas por Categoria', fontweight='bold')

# 4.4 Histograma - Distribuicao dos valores de venda
plt.subplot(2, 3, 4)
plt.hist(df_vendas['valor_venda'], bins=8, color='#4ECDC4', alpha=0.7, edgecolor='black')
plt.title('Distribuicao dos Valores de Venda', fontweight='bold')
plt.xlabel('Valor da Venda (R$)')
plt.ylabel('Frequencia')

# 4.5 Boxplot - Analise de valores por categoria
plt.subplot(2, 3, 5)
sns.boxplot(data=df_vendas, x='categoria', y='valor_venda')
plt.title('Distribuicao de Valores por Categoria', fontweight='bold')
plt.xlabel('Categoria')
plt.ylabel('Valor da Venda (R$)')
plt.xticks(rotation=45)

# 4.6 Heatmap - Vendas por categoria e mes
plt.subplot(2, 3, 6)
pivot_table = df_vendas.pivot_table(values='valor_venda', 
                                   index='categoria', 
                                   columns='mes', 
                                   aggfunc='sum', 
                                   fill_value=0)

sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Vendas por Categoria e Mes', fontweight='bold')
plt.xlabel('Mes')
plt.ylabel('Categoria')

plt.tight_layout()
plt.show()

# PASSO 5: CONCLUSAO E ANALISE DE INSIGHTS
print("\n5. CONCLUSOES E INSIGHTS...")
print("="*60)

print("\nPRINCIPAIS INSIGHTS IDENTIFICADOS:")

# Categoria com maior faturamento
categoria_top = vendas_por_categoria['Total_Vendas'].idxmax()
valor_categoria_top = vendas_por_categoria.loc[categoria_top, 'Total_Vendas']

print(f"\n1. CATEGORIA MAIS LUCRATIVA:")
print(f"   • {categoria_top} representa {(valor_categoria_top/total_vendas)*100:.1f}% do faturamento total")
print(f"   • Valor total: R$ {valor_categoria_top:,.2f}")

# Mes com maior faturamento
mes_vendas = df_vendas.groupby('mes')['valor_venda'].sum()
mes_top = mes_vendas.idxmax()
valor_mes_top = mes_vendas.max()

print(f"\n2. SAZONALIDADE:")
print(f"   • Mes {mes_top} teve o maior faturamento: R$ {valor_mes_top:,.2f}")
print(f"   • Variacao entre meses indica possivel sazonalidade")

# Ticket medio por categoria
print(f"\n3. TICKET MEDIO POR CATEGORIA:")
for categoria in vendas_por_categoria.index:
    ticket_medio = vendas_por_categoria.loc[categoria, 'Venda_Media']
    print(f"   • {categoria}: R$ {ticket_medio:,.2f}")

print(f"\nSUGESTOES PARA A EMPRESA:")
print(f"\n1. FOCO EM CATEGORIAS RENTAVEIS:")
print(f"   • Investir mais em {categoria_top} (categoria mais lucrativa)")
print(f"   • Desenvolver promocoes especificas para esta categoria")

print(f"\n2. ESTRATEGIAS SAZONAIS:")
print(f"   • Preparar estoque adequado para o mes {mes_top}")
print(f"   • Criar campanhas para meses com menor movimento")

print(f"\n3. DIVERSIFICACAO:")
print(f"   • Expandir variedade de produtos nas categorias menos representadas")
print(f"   • Analisar margem de lucro para otimizar mix de produtos")

print(f"\n4. ANALISE DE TENDENCIAS:")
print(f"   • Monitorar evolucao mensal para identificar padroes")
print(f"   • Implementar sistema de alertas para quedas de performance")

# Fechar conexao com banco de dados
conexao.close()
print(f"\nConexao com banco de dados encerrada.")
print("="*60)
print("ANALISE CONCLUIDA COM SUCESSO!")
print("="*60)
