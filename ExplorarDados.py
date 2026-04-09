#%%

import pandas as pd
import numpy as np

df = pd.read_csv("TabelaMusicas.csv", sep=',', low_memory=False)

#%%

print(f"Quantidades de plays a cada ano: \n {df.groupby(by="ano")["Nome_Musica"].count()}")

print("-"*40)
print(f"Quantidades de plays com músicas ouvidas por pelo menos 1 min em cada ano: \n {df[df["MinutosEscutados"] >= 1].groupby(by="ano")["Nome_Musica"].count()}")

#%%
print("-"*40)
print(f"Quantidades de horas escutadas em cada ano: {df.groupby(by="ano")["HorasEscutadas"].sum()}")


#%%

print(f"Quantidade de minutos ouvidos em 2025 até o mes de novembro: {round(np.sum(df["MinutosEscutados"][(df["ano"]==2025) & (df["mes"]<=11)]),2)}")

#%%
# TOP 10 bandas mais escutadas de todos os tempos
df_bandas = (((df[df["MinutosEscutados"]>1]).groupby(by="artista")
                            .agg(
                            {"Nome_Musica":'count',
                             "HorasEscutadas":'sum'}
                            )).rename(columns={"Nome_Musica":"QuantidadeMusicas"})
                            .sort_values(by="HorasEscutadas", ascending=False))
df_bandas["HorasEscutadas"] = round(df_bandas["HorasEscutadas"],2)
df_bandas
#%%

df_filtro = df[(df["ano"]==2025) & (df["mes"].between(0,8))]

df_musicas = (df_filtro.groupby(by=["Nome_Musica","artista"])
                            .size()
                            .reset_index(name="qnt_plays")
                            .sort_values(by="qnt_plays",ascending=False))
df_musicas
