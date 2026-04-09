#%%

import pandas as pd

df = pd.read_csv("TabelaMusicas.csv", sep=',', low_memory=False)
#%%
df_musicas = df

def validar_mes(mes):
    if not 1 <= mes <= 12:
        raise ValueError(f"Mês {mes} inválido")
    return mes
    
def validar_mes_final(mesInicio, mesFinal):
    if mesInicio > mesFinal:
        raise ValueError("O mês inicial não pode ser maior que o mês final")
    
def validar_ano_final(anoInicio, anoFinal):
    if anoInicio > anoFinal:
        raise ValueError("O ano inicial não pode ser maior que o ano final")
    
def MusicasPeriodoAno():
    try:

        anoInicio = int(input("Insira o ano inicial desejado: "))
        anoFinal = input("Insira o ano final desejado: ").strip()

        if not anoFinal:

            mesInicio = validar_mes(int(input("Insira o primeiro mês desejado: ")))
            mesFinal = validar_mes(int(input("Insira o ultimo mês desejado: ")))

            validar_mes_final(mesInicio,mesFinal)
        
            df_filtro = (df_musicas[(df_musicas["ano"]==anoInicio) & 
            (df_musicas["mes"].between(mesInicio,mesFinal))])

            print(f"Músicas ouvidas em {anoInicio}, do mês {mesInicio}, até o mês {mesFinal}")

        else:
            anoFinal = int(anoFinal)
            validar_ano_final(anoInicio,anoFinal)
            df_filtro = (df_musicas[(df_musicas["ano"].between(anoInicio,anoFinal))])

            print(f"Músicas ouvidas entre {anoInicio} e {anoFinal}")

    except ValueError as e:
        print(f"Erro: {e}")
        return

    if df_filtro.empty:
        print("Nenhum dado encontrado para esse período.")
        return

    df_final = (df_filtro.groupby(by=["Nome_Musica","artista"])
                            .agg(qnt_plays = ("Nome_Musica",'size'),
                            minutos_ouvidos = ("MinutosEscutados", "sum"))
                            .reset_index()
                            .sort_values(by="minutos_ouvidos",ascending=False))
    df_final["minutos_ouvidos"] = round(df_final["minutos_ouvidos"],2)
    df_final["horas_ouvidas"] = round((df_final["minutos_ouvidos"]/60),2)

    df_final = df_final.reset_index(drop=True)
    df_final.index = df_final.index + 1  

    return df_final

MusicasPeriodoAno()
