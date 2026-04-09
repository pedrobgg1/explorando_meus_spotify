#%%
import pandas as pd
import glob

jsons = glob.glob("Spotify Extended Streaming History/*.json")

df = pd.concat(
    [pd.read_json(arquivo) for arquivo in jsons],
    ignore_index=True
)

df_filtro = (df[["master_metadata_album_artist_name",
                 "master_metadata_track_name",
                 "master_metadata_album_album_name",
                 "ms_played",
                 "offline",
                 "skipped",
                 "shuffle",
                 "platform",
                 "ts"]]).copy()


df_colunas = (df_filtro.rename(columns={"master_metadata_track_name":"Nome_Musica",
                                        "master_metadata_album_album_name":"Nome_album",
                                        "master_metadata_album_artist_name":"artista"})
                                        .copy())

df_colunas["ts"] = pd.to_datetime(df_colunas["ts"])

df_colunas["ano"] = df_colunas["ts"].dt.year
df_colunas["mes"] = df_colunas["ts"].dt.month
df_colunas["hora"] = df_colunas["ts"].dt.hour

df_colunas["ts"] = df_colunas["ts"].dt.date

df_colunas["MinutosEscutados"] = round(df_colunas["ms_played"] / 60000,4)
df_colunas["HorasEscutadas"] = round(df_colunas["MinutosEscutados"] / 60, 4)

df_final = df_colunas.dropna().copy()

df_final.to_csv("TabelaMusicas.csv", sep=',', index=False)