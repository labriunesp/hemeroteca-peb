# Hemeroteca de Política Externa Brasileira

- [Informações sobre o projeto](https://apoio.labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro)

|Informação | Link |
|-----------|------|
|Atividades realizadas| [Link](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro#atividades-realizadas)|
|Próximas atividades| [Link](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro#proximas-atividades)|

- Diretório com os dados da Hemeroteca /media/hdvm07/bd/002/997/001

## Próximos passos

 - Titulo_noticia: 
 - Data
 

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
|titulo|vazio|`/media/hdvm08/bd/002/997/001/tif/07-brasil-eua/2007-03-10--.tif`|9|
|titulo | page |`/media/hdvm08/bd/002/997/001/tif/02-brasil-america_latina/1996-02-05_ESP_page0001.tif`|41|
| |  |

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