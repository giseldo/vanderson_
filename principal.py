# dependencias que precisam ser instaladas
# c:\> pip install pandas
# c:\> pip install openpyxl

import pandas as pd
# importa o seu excel para um dataframe
df = pd.read_excel("teste.xlsx")
# exiba as colunas
print(df.columns)
# calcula a média de uma coluna numerica
print(df["notas"].mean)


