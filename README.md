# Hemeroteca de Política Externa Brasileira

- [Informações sobre o projeto](https://apoio.labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro)

|Informação | Link |
|-----------|------|
|Atividades realizadas| [Link](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro#atividades-realizadas)|
|Próximas atividades| [Link](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro#proximas-atividades)|

- Diretório com os dados da Hemeroteca /media/hdvm07/bd/002/997/001

## Tarefas

 - deslocar siglas para nomes dos jornais (metadados_bons) - Thiago
 - verificar silgas "NA" (metadados_bons) - Thiago
 - verificar as datas (metadados_ruins)
 

## Metadados

|Informação | Tipo |
|-----------|------|
|Data | `str`|
|Sigla jornal | `str`|
|Nome Jornal| `str`|
|Título notícia | `str`|
|Nome arquivo tif | `list`|
|Nome arquivo pdf | `list`|
|Número de páginas | `int`|
|Tema | `list`
|Verifica OCR | `bool`|
|Diretório base | `str`|
|Diretório arquivo |`str`|
|Código base | `str`|


## Metadados bons

|entrada | problema |exemplo|quantidade|
|-----------|------|------|---------|
|titulo|vazio|`/media/hdvm08/bd/002/997/001/tif/07-brasil-eua/2007-03-10--.tif`|25|
|titulo | page |`/media/hdvm08/bd/002/997/001/tif/02-brasil-america_latina/1996-02-05_ESP_page0001.tif`|41|
|titulo|sigla jornal no titulo| `/media/hdvm08/bd/002/997/001/tif/02-brasil-america_latina/1997-05-16_B_FSP.tif` | 191 |
|sigla jornal|titulo inteiro ou primeira palavra do título no campo da sigla| `/media/hdvm08/bd/002/997/001/tif/12-brasil-politica_exterior/1993-12-14-Acordo_no_GATT_reduzira_a_pressao_inflacionaria.tif` | 70+ |
|sigla jornal|"1" ou "0000" no lugar da sigla|`/media/hdvm08/bd/002/997/001/tif/06-brasil-economia_internacional/2004-08-04-0000-OMC_pode_facilitar_negociação_com_UE.tif`|7|
|nome do jornal|campo vazio (NA), mesmo que o campo de siglas esteja preenchido|casos em que a sigla é JB, JT, JC, OESP, valor, globo, fl, fsd, clarin, exame, ec, etc| `/media/hdvm08/bd/002/997/001/tif/03-brasil-argentina/2000-08-03-Valor-Impasse_breca_acordo_automotivo_do_Mercosul.tif` | 340+ |
|titulo|numero|"1" ou "2" ou "0000"| `/media/hdvm08/bd/002/997/001/tif/12-brasil-politica_exterior/0000-03-01--1.tif` | 13 |
|jornal sigla | NA | 230 |

## Metadados com problemas

|entrada | problema |exemplo|quantidade|
|-----------|------|------|---------|
| sigla jornal | NA | "/media/hdvm08/bd/002/997/001/tif/12-brasil-politica_exterior/1985-05-16-Setúbal_defenae_diplomacia_mediadora_page0001.tif" | 4 |
| nome do jornal | NA | "/media/hdvm08/bd/002/997/001/tif/12-brasil-politica_exterior/1985-05-16-Setúbal_defenae_diplomacia_mediadora_page0001.tif" | 4 |


## Metadados ruins

|entrada | problema |exemplo|quantidade|
|-----------|------|------|---------|

## Comandos para trabalhar no projeto
```
cd codigo/hemeroteca-peb
code .
git pull origin main && conda activate env_hemeroteca-peb
git checkout thiago-vicino
```

```
conda config --set pip_interop_enabled True
conda config --set env_prompt '({name})'
conda config --add envs_dirs ./env
touch environment.yml && conda env create -f environment.yml
git pull origin main && conda activate env_hemeroteca-peb && conda env update --prune

```

# Apontamentos do trabalho

- Os arquivos da Hemeroteca estão no formato TIF. Uma parte deles possui apenas uma página (época Kelly e Ricardo) e outra mais de uma página (época da Regiane).
  - [ ] Verificar quantidade de arquivos de cada uma dessa épocas.
  - [ ] Verificar arquivos colocados nas seguintes páginas:
      - /media/hdvm07/bd/002/997/001/Antiga/hemeroteca-peb-metadados/arquivos-renomeados/pendencia/arquivos/ALOCAR01
      - /media/hdvm07/bd/002/997/001/Antiga/hemeroteca-peb-metadados/arquivos-renomeados/pendencia/arquivos/alocar02

  - [ ] Pasta 02, 03 e 07 - Ana Mota
  - [ ] Pasta 08 e 12 - Thiago



# Comentário Ana
```
[20:01, 09/03/2022] Ana Julia: 10/03/2022 – Visualização dos erros presentes no json3
Data: Como algumas datas não foram declaradas, pensei em usar o datatime, como é um módulo que permite formatar datas acho que poderia ser uma ideia. Mas, não sei se seria possível renomear essas datas através disso ou se ele apenas formata datas do dia atual.
Sigla e Nome do jornal: Pensei em usar o rename, mas citar as colunas que estão tendo problema. Pelo fato de ser muitas colunas não sei se seria uma boa ideia usar esse método. 
dir_arquivo: Alguns problemas que estão dando depois da última barra (acredito que por algumas datas estarem com problemas) é de que algumas datas não estão sendo “printadas”.

[20:02, 09/03/2022] Ana Julia: Não sei se era exatamente isso que vc queria, mas tentei colocar algumas ideias no "papel".

```
# https://stackoverflow.com/questions/21646245/how-to-decode-a-text-with-unicodes-like-u00e7-in-python

## Arquivos com imagens ruins:
0000-00-00-ESP-Alan_garcia_amanha_em-p01.tif

## TODO
>pesquisar no json os termos abaixo e comparar arquivos da pasta tif-bkp-comparar com arquivos da pasta tif para incluir os arquivos que foram sobrescritos 
_t-p02 (substituir no json o _t-p01 por -p01 e assim por diante [FEITO!!!!!])
_t- (conferir na pasta tif, pois tem uns 4 arquivos com esse elemento que precisam ser renomeados [FEITO!!])
_ti-p02 ([FEITO!!])
ver em: hemeroteca_01_ajuste_renomear.py
> depois: renomear nomes dos arquivos no json tirando os termos pesquisados acima [FEITO!!!!!]
15/08/2022
>Usar TinyDB para apagar entradas com titulo: [apagar] [FEITO!!!!!]