# -*- coding: utf-8 -*-
"""Immigration to Canada

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UBfI3fiKAA9suux2KIHpN2JHPTVUf2dG
"""

'''
██╗███╗░░░███╗███╗░░░███╗██╗░██████╗░██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗  ████████╗░█████╗░
██║████╗░████║████╗░████║██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║  ╚══██╔══╝██╔══██╗
██║██╔████╔██║██╔████╔██║██║██║░░██╗░██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║  ░░░██║░░░██║░░██║
██║██║╚██╔╝██║██║╚██╔╝██║██║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║  ░░░██║░░░██║░░██║
██║██║░╚═╝░██║██║░╚═╝░██║██║╚██████╔╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║  ░░░██║░░░╚█████╔╝
╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░

░█████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██╔██╗██║███████║██║░░██║███████║
██║░░██╗██╔══██║██║╚████║██╔══██║██║░░██║██╔══██║
╚█████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝

# Projeto por Eduardo Coqueiro para estudos na plataforma Alura
# Data: 06/07/2024

'''

"""Biblioteca: https://www.kaggle.com/datasets/ammaraahmad/immigration-to-canada

Uma empresa que presta serviços de consultoria e aconselhamento para pessoas que querem migrar do Brasil para o Canadá deseja melhorar os seus serviços. Para isso, temos alguns arquivos que foram disponibilizados para fazer uma análise das tendências de imigração do Brasil dos últimos anos.

Entre esses arquivos, há um arquivo CSV chamado "imigrantes-canada" que contém informações de todos os países com os números aproximados de imigrantes para o Canadá para cada um dos anos desde 1980. Vamos trabalhar com esse arquivo.
"""

# Trazendo o kaggle:

!pip install -q kaggle

# Pegando o dataset diretamente do Kaggle via API:

from google.colab import files
files.upload() # Aqui é basicamente para eu upar a API do meu Kaggle!

# Baixando o dataset:
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d ammaraahmad/immigration-to-canada

#Extraindo o arquivo .zip:

!unzip immigration-to-canada

# Chamando as bibliotecas que vamos usar:

import pandas as pd
import seaborn as plt
import matplotlib.pyplot as plt
import plotly.express as px

# Criando e lendo o nosso data frame para conferir se está tudo correto:

df = pd.read_csv('/content/canadian_immegration_data.csv')
df.head()

# Pegando mais algumas informações do nosso data frame:

df.info()

"""### Analisando as tendências de imigração do Brasil em um determinado período"""

# Mudando o index para o país:

df.set_index('Country', inplace = True)
df.head()

# Criando variáveis para armazenar os intervalos de tempo (facilitando a analise):

anos = list(map(str, range(1980, 2014)))
anos

# Pegando o rótulo específico do Brasil:

brasil = df.loc['Brazil', anos]
brasil.head()

# Criando o dataframe com os dados do brasil

brasil_dict = {'Ano': brasil.index.tolist(),
                'Imigrantes': brasil.values.tolist()}

brasil_dados = pd.DataFrame(brasil_dict) # Criando o dataframe!
brasil_dados

import matplotlib.pyplot as plt

# Gerando o gráfico de linhas para acompanhar melhor:

plt.figure(figsize=(12, 8))
plt.title('Imigrantes do Brasil')
plt.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2020'])
plt.xlabel('Anos')
plt.ylabel('Número de imigrantes')

plt.show()

# Exercício 1: Fazer o comparativo Brasil x Argentina:

# Especificando dados da argentina:
argentina = df.loc['Argentina', anos]
argentina.head()

# Criando o titulo do data frame:
argentina_dict = {'Anos': argentina.index.tolist(),
                  'Imigrantes': argentina.values.tolist()}

# Criando o data frame:
argentina_dados = pd.DataFrame(argentina_dict)

# Printando o data frame:
argentina_dados.head()

# Criando o gráfico da Argentina:

plt.figure(figsize = (12, 8))
plt.plot(argentina_dados['Anos'], argentina_dados['Imigrantes'])
plt.title('Imigrantes da Argentina')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2020'])
plt.xlabel('Anos')
plt.ylabel('Número de Imigrantes')

plt.show

# Juntando ambos os gráficos:

plt.figure(figsize = (12, 8))
plt.plot(argentina_dados['Anos'], argentina_dados['Imigrantes'])
plt.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
plt.title('Imigrantes da Argentina e Brasil')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010', '2020'])
plt.xlabel('Anos')
plt.ylabel('Número de Imigrantes')
plt.legend(['Argentina', 'Brasil'])  # Lista de rótulos

plt.show()

# Para customizar ainda mais esses gráficos, precisamos criar um figura:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020')
ax.set_xlabel('Anos')
ax.set_ylabel('Imigrantes')
plt.show()

# Agora vamos criar mais de um gráfico por figura

fig, axs = plt.subplots(1, 2, figsize = (15, 5))

axs[0].plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020')
axs[0].set_xlabel('Anos')
axs[0].set_ylabel('Imigrantes')
axs[0].grid()

axs[1].boxplot(brasil_dados['Imigrantes'])
axs[1].set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número de Imigrantes')
axs[1].grid()


plt.show()

"""### O boxplot nos permite ver algumas coisas:

- O valor máx e mínimo de imigrantes
- Percebemos que em 25% dos anos o número de imigrantes foi próximo a 500, 50% (linha central) o número de imigrantes foi entre 500 e 1000, e a linha superior nos mostra que em 75% dos anos tivemos em torno de 1000 imigrantes. Para validar isso vamos usar o describe() do pandas
"""

brasil_dados.describe()

"""#### Com isso vemos os valores exatos!"""

# Agora vamos analisar as tendências de migração de uma forma geral para 4 países da américa latina (Brasil, Colômbia, Argentina e Peru.)

fig, axs = plt.subplots(2, 2, figsize = (10,6))
fig.subplots_adjust(hspace = 0.5, wspace = 0.3)
fig.suptitle('Imigrantes por ano na América latina de \n 1980 a 2020')

axs[0,0].plot(df.loc['Brazil', anos])
axs[0,0].set_title('Brazil')

axs[0,1].plot(df.loc['Colombia', anos])
axs[0,1].set_title('Colombia')

axs[1,0].plot(df.loc['Argentina', anos])
axs[0,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru', anos])
axs[1,1].set_title('Peru')

for ax in axs.flat:
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))
  ax.set_xlabel('Anos')
  ax.set_ylabel('Imigrantes')

for ax in axs.ravel():
  ax.set_ylim(0, 7000)

"""### Desafio 1:

Você trabalha como Analista de Dados em uma empresa de varejo e recebeu a tarefa de criar uma figura com subplots que apresente a variação no número de vendas em quatro diferentes lojas ao longo de um ano. A gerência da empresa precisa visualizar de forma clara as tendências de vendas em cada loja, para que possam tomar decisões estratégicas sobre os estoques e ações de marketing. Para isso, você deve criar quatro subplots dispostos em duas linhas e duas colunas, onde cada subplot representa uma loja diferente. Nesse desafio, cada subplot deve apresentar um gráfico de linhas que mostre a variação do número de vendas ao longo dos meses do ano.


"""

# Desafio 1:

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

# Separando as lojas

dt = pd.DataFrame(vendas_2022)

# Criando a coluna para lojas
dt['Lojas'] = lojas

# Redefinindo o index em função de loja:
dt.set_index('Lojas', inplace=True)

# Vendo o dataframe final:

dt.head()

# Consttuindo os gráficos:
fig, axs = plt.subplots(2, 2, figsize = (12, 10))

# Ajustar os espaçamentos entre os subplots
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.suptitle('Vendas nas 4 lojas ao longo do ano: ')

axs[0,0].plot(dt.loc['A'])
axs[0,0].set_title('Loja A')

axs[0,1].plot(dt.loc['B'])
axs[0,1].set_title('Loja B')

axs[1,0].plot(dt.loc['C'])
axs[1,0].set_title('Loja C')

axs[1,1].plot(dt.loc['D'])
axs[1,1].set_title('Loja D')

# Colocando o grid e titulos
for ax in axs.flat:
  ax.grid()
  ax.set_xlabel('Meses')
  ax.set_ylabel('Valores')

# Colocando min e máx (0 e 450):
for ax in axs.ravel():
  ax.set_ylim(0, 450)

# Módulo 3: Custumizando

# Mudando o tamanho do titulo

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18)
ax.set_xlabel('Anos')
ax.set_ylabel('Imigrantes')
plt.show()

# Mudando o tamanho do eixo x e y:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.show()

# Mudando o tamanho dos ticks do gráfico (x e y):

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18)
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.show()

# Mudando o titulo para alinhamento ao lado esquerdo:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'])
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18, loc = 'left')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.show()

# Mudando a espessura da linha:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'], lw = 3)
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18, loc = 'left')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.show()

# Adicionando marcadores:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'], lw = 3, marker = 'h')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18, loc = 'left')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.show()

''''o': círculo
'.': ponto
',': pixel
'x': x
'+'': sinal de mais
'v': triângulo apontando para baixo
'^': triângulo apontando para cima
'<': triângulo apontando para a esquerda
'>': triângulo apontando para a direita
's': quadrado
'd': diamante
'D': diamante grande
'p': pentágono
'h': hexágono
'H': hexágono grande
'*': estrela
'1': estrela de 1 ponto (parecida com um triângulo)
'2': estrela de 2 pontos
'3': estrela de 3 pontos
'4': estrela de 4 pontos
'|': linha vertical
'_': linha horizontal'''

# Adicionando grade novamente, dessa vez mais suave:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'], lw = 3, marker = 'h')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18, loc = 'left')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.grid(linestyle = '--')
plt.show()

# Mudando as cores:

fig,ax = plt.subplots(figsize = (12,8))
ax.plot(brasil_dados['Ano'], brasil_dados['Imigrantes'], lw = 3, marker = 'h', color = 'g')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.set_title('Número de imigrantes do Brasil para o canada dos anos \n 1980 até 2020', fontsize = 18, loc = 'left')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)
ax.set_xlabel('Anos', fontsize = 14)
ax.set_ylabel('Imigrantes', fontsize = 14)
plt.show()

df

df['Region'].unique()

# Vamos trabalhar com todos os países da América do sul para termos mais variáveis

america_sul = df.query("Region == 'South America'")


fig, ax = plt.subplots(figsize = (16,8))
ax.bar(america_sul.index, america_sul['Total'], color = 'g')

america_sul.head()

# Mudando para um gráfico de barras invertido, pois fica melhor

fig, ax = plt.subplots(figsize = (16,8))
ax.barh(america_sul.index, america_sul['Total'], color = 'g')

# Vamos melhorar ainda mais:

# Vamos ordenar:

america_sul_ordenado = america_sul.sort_values('Total', ascending = True)

# Gerando o gráfico com eles ordenados:

fig, ax = plt.subplots(figsize = (16,8))
ax.barh(america_sul_ordenado.index, america_sul_ordenado['Total'], color = 'g')

# Fica bem melhor, mas vamos fazer outras melhorias:

fig, ax = plt.subplots(figsize = (20,8))

# Criando uma lista de cores
colors = plt.cm.get_cmap('Set3', len(america_sul))

ax.barh(america_sul_ordenado.index, america_sul_ordenado['Total'], color=[colors(i) for i in range(len(america_sul))])

# Rotacionando os rótulos do eixo x para melhor visualização
ax.set_xticklabels(america_sul.index, rotation=45, ha='right', fontsize=10)

# Adicionando rótulos aos eixos
ax.set_xlabel('Países', fontsize=12)
ax.set_ylabel('Total', fontsize=12)

# Adicionando um título ao gráfico
ax.set_title('Total por País na América do Sul', fontsize=15)

# Mostrando o gráfico
plt.tight_layout()
plt.show()

# Vamos criar um que o Brasil possui uma cor diferente dos demais, tendo destaque:

cores = []
for pais in america_sul_ordenado.index:
    if pais == 'Brazil':
        cores.append('g')
    else:
        cores.append('silver')

fig, ax = plt.subplots(figsize = (16,8))
ax.barh(america_sul_ordenado.index, america_sul_ordenado['Total'], color = cores)

# Fazendo anotações na figura:

# código omitido
fig, ax = plt.subplots(figsize=(12, 5))
ax.barh(america_sul_ordenado.index, america_sul_ordenado['Total'], color=cores)
ax.set_title('América do Sul: Brasil foi o quarto país com mais imigrantes\npara o Canadá no período de 1980 a 2013', loc='left', fontsize=16)
ax.set_xlabel('Número de imigrantes', fontsize=14)
ax.set_ylabel('')
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_tick_params(labelsize=12)
ax.set_frame_on(False) # Retira as bordas (box)
ax.get_xaxis().set_visible(False) #Retirando o eixo x
ax.tick_params(axis='both', which='both', length=0)

for i, v in enumerate(america_sul_ordenado['Total']):
    ax.text(v + 20, i, str(v), color='black', fontsize=10, ha='left', va='center')

plt.show()

# Salvando o gráfico:
fig.savefig('Gráfico teste', transparent = True, dpi = 300, bbox_inches = 'tight')

"""### Desafio 2:

Mais uma etapa de desafio se inicia! Aproveite a oportunidade proposta e mergulhe nas possibilidades. Na aula anterior, você teve o desafio de criar uma figura com subplots que apresentam a variação no número de vendas em quatro diferentes lojas ao longo de um ano. Agora é o momento de elevar essa figura a um novo patamar! É a hora de personalizá-la! Nesta segunda parte do desafio, você deve explorar as opções de customização dos subplots para deixar a figura mais clara e atraente para a gerência da empresa.

Algumas ideias de customização que você pode explorar são:

Alterar a posição dos títulos dos subplots para esquerda.
Aumentar o tamanho da fonte do título geral da figura para destacá-lo.
Aumentar o tamanho dos títulos e rótulos dos eixos dos subplots.
Deixar as linhas com a espessura maior.
Alterar a cor das linhas de cada loja para diferenciá-las ainda mais.
Fique à vontade para testar mais customizações!

E mais uma dica: você pode reduzir o tamanho do código utilizando o comando for i, ax in enumerate(axs.flat): que permite um loop iterando sobre todos os subplots da figura. Dentro desse loop você pode passar as funções plot, set_title, set_xlabel, set_ylabel e etc…

Lembrando que os dados são os seguintes:
"""

# Desafio 2:

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

# DESAFIO ANTERIOR:

# Separando as lojas

dt = pd.DataFrame(vendas_2022)

# Criando a coluna para lojas
dt['Lojas'] = lojas

# Redefinindo o index em função de loja:
dt.set_index('Lojas', inplace=True)

# Vendo o dataframe final:

dt.head()

# Consttuindo os gráficos:
fig, axs = plt.subplots(2, 2, figsize = (12, 10))

cores = ['darkviolet', 'green', 'darkblue', 'coral']

# Ajustar os espaçamentos entre os subplots
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.suptitle('Vendas nas 4 lojas ao longo do ano: ', fontsize=16)

axs[0,0].plot(dt.loc['A'])

axs[0,1].plot(dt.loc['B'])

axs[1,0].plot(dt.loc['C'])

axs[1,1].plot(dt.loc['D'])

# Colocando o grid e titulos
for ax in axs.flat:
  ax.grid()
  ax.set_xlabel('Meses')
  ax.set_ylabel('Valores')

# Colocando min e máx (0 e 450):
for ax in axs.ravel():
  ax.set_ylim(0, 450)

#Loop para plotar e customizar os subplots
for i, ax in enumerate(axs.flat):
    ax.plot(dt.loc[dt.index[i]], color=cores[i], lw=3)
    ax.set_title(f'Vendas na loja {dt.index[i]}', loc='left', fontsize=16)
    ax.set_xlabel('Mês', fontsize=14)
    ax.set_ylabel('Número de vendas', fontsize=14)
    ax.tick_params(labelsize=12)
    ax.grid(color='lightgrey')

df

# Agora vamos trabalhar com o seaborn:

import seaborn as sns

# Criaremos uma função para repetira a criação dos gráficos:

top_10 = df.sort_values('Total', ascending = False). head(10)
top_10

def criando_graficos(df, palette):
  sns.set_theme()
  fig, ax = plt.subplots(figsize = (10,8))
  sns.barplot(data = df, y = df.index, x = 'Total', orient = 'h', palette = palette)
  ax.set(title = 'Países com maior imigração para o Canadá\n1980 a 2013',
         xlabel = 'Total de imigrantes',
         ylabel = 'Países')
  sns.despine()
  plt.show()

# Testando nossa função que recebe 2 argumentos:

criando_graficos(top_10, 'rocket')

"""### Desafio 3:

Parabéns por chegar até aqui, em mais um desafio! Voltando aos dados utilizados no projeto que nós estamos desenvolvendo neste curso, agora chegou o momento de utilizar todos os conhecimentos adquiridos sobre as bibliotecas Matplotlib e Seaborn.

Nesta etapa, seu desafio é criar uma figura contendo as tendências de imigração dos 4 maiores países da América latina: Brasil, Argentina, Peru e Colômbia. Através dessa criação você pode explorar diversas possibilidades e reconhecer de forma atrativa o seu processo de desenvolvimento.E não nos esqueçamos das orientações! Essa figura precisa ter uma linha para cada país, título, rótulos nos eixos, cores apropriadas, um tema da biblioteca Seaborn e legenda. Por isso, pense nas questões de acessibilidade, como tamanho das fontes e espessura das linhas. É importante escolher cores adequadas que não causem cansaço visual ou dificultem a leitura das informações. Além disso, o tamanho das fontes deve ser legível o suficiente para que as pessoas possam interpretar os dados com facilidade.
"""

america_sul = df.query("Region == 'South America'")
america_sul

# Desafio 3:

# Brasil, Argentina, Peru e Colômbia: Criando meu dataframe!

paises = {'Brazil', 'Argentina', 'Peru', 'Colombia'}

big_4 = america_sul[america_sul.index.isin(paises)]

big_4

# Gerando o gráfico:

def graf_america(da, palette):
  fig, ax = plt.subplots(figsize = (12,8))
  ax = sns.barplot(data = da, x = 'Total', y = da.index, palette = palette, orient = 'h')
  ax.set(title = 'Maiores países da América do Sul em extensão territorial',
           ylabel='Países',
           xlabel='Número de imigrantes')

  for i,v in enumerate(da['Total']):
    ax.text(v + 32, i, str(v), color='black', fontsize=10, ha='left', va='center')  # Corrigido

  ax.get_xaxis().set_visible(False)  # Corrigido
  sns.despine()
  plt.show()

graf_america(big_4, 'rocket')

# Vamos criar gráficos mais interativos usando a biblioteca plotly

# Inicialmente para Brasil:

# Criando o gráfico:
fig = px.line(brasil_dados, x='Ano', y='Imigrantes',
              title='Imigração do Brasil para o Canadá no período de 1980 a 2013', markers = True)
fig.update_traces(line_color='green', line_width=4)
fig.update_layout(
    width=1000, height=500,
    xaxis={'tickangle': -45},
    font_family='Arial',
    font_size=14,
    font_color='grey',
    title_font_color='black',
    title_font_size=22,
    xaxis_title='Ano',
    yaxis_title='Número de imigrantes')
fig.write_html('Imigração do Brasil para o Canadá no período de 1980 a 2013.html')
fig.show()

# Para america do sul
df_america_sul_clean = america_sul.drop(['Continent', 'Region', 'Total'], axis=1)
america_sul_final = df_america_sul_clean.T
america_sul_final

fig = px.line(america_sul_final, x=america_sul_final.index, y=america_sul_final.columns, color='Country',
              title='Imigração dos países da América do Sul para o Canadá de 1980 a 2013')
fig.update_layout(
    xaxis={'tickangle': -45},
    xaxis_title='Ano',
    yaxis_title='Número de imigrantes')
fig.write_html('Imigração dos países da América do Sul para o Canadá de 1980 a 2013.html')
fig.show()