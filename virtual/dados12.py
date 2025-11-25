import pandas as pd

'''df = pd.read_csv('ClassicDisco.csv')

#Filtrar músicas lançadas depois de 1980, mostre apenas as colunas 'Year' e 'Track'
print(df[df['Year']> 1980][['Year', 'Track']])'''

dados = [10, 20, 30, 40]
#Criar série
serie = pd.Series(dados, index=['A', 'B', 'C', 'D'])
print(serie)