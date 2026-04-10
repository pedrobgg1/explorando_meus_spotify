# Análise de Histórico do Spotify

Este projeto foi criado por curiosidade própria para explorar os dados do meu Spotify, mas também serve como uma ótima prática em Python, especialmente para manipulação e tratamento de dados.

## Como usar

### Baixe seus dados do Spotify
* Solicite o Extended Streaming History nas configurações de privacidade da sua conta.
* Após receber os arquivos, extraia o .zip.

### Configure o caminho dos arquivos
* No arquivo preparacaodabase.py, insira o caminho da pasta onde estão os arquivos JSON baixados.

### Prepare a base de dados
* Execute o arquivo preparacaodabase.py para carregar e organizar os dados.

### Utilize as funções de análise

No arquivo funcaoanomes.py, foi criada a função:

**MusicasPeriodoAno()**

Ao chamar essa função, você precisará colocar:

* **AnoInicial:** Escolha um ano para inciar a busca das músicas
* **AnoFinal:** Ao colocar um ano final você irá conseguir todas as musicas ouvidas entre o ano incial e final

Caso você deixe o AnoFinal em branco, será pedido para indicar o período mensal escolhido
* **MesInicial:** O número posto indicará em qual mês a busca começará
* **MesFinal:** O número posto indicará em qual mês a busca terminará

-----------------------------------------------------------
**EX:**

AnoInicial = 2022

AnoFinal = 2023

**Resultado** = Músicas ouvidas entre 01/2022 e 12/2023

-----------------------------------------------------------

AnoInicial = 2022

AnoFinal = 

MesInicial = 3

MesFinal = 7

**Resultado** = Músicas ouvidas entre 03/2022 e 07/2022


## Observações
O projeto utiliza dados reais exportados do Spotify.
É uma forma prática de treinar:
* Manipulação de dados com pandas
* Validação de inputs
* Organização de código em funções

## Conclusão
Foi possível explorar padrões de consumo musical ao longo do tempo e, de quebra, relembrar músicas esquecidas enquanto pratica Python na vida real.