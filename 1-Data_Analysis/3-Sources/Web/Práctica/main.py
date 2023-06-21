import functions as fun
import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))


offset = 0
nombre_archivo = 'df_a.csv'
df_concatenated = []

while True:

    df_created = fun.create_df(offset= offset, inicial= 'a')

    if df_created.shape[0] < 100:
          df_concatenated.append(df_created)
          break

    else:
         offset += 100
         df_concatenated.append(df_created)

df_final = pd.concat(df_concatenated)
df_final.reset_index(inplace=True, drop=True)
df_final.to_csv(nombre_archivo)





