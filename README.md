# Hemeroteca de Política Externa Brasileira

- [Informações sobre o projeto](https://apoio.labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro)

|Informação | Link |
|-----------|------|
|Atividades realizadas| [Link](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro#atividades-realizadas)|
|Próximas atividades| [Link](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro#proximas-atividades)|

- Diretório com os dados da Hemeroteca /media/hdvm07/bd/002/997/001

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
git pull origin main && conda activate env_hemeroteca-peb
conda env update --prune


```

# Apontamentos do trabalho

- Os arquivos da Hemeroteca estão no formato TIF. Uma parte deles possui apenas uma página (época Kelly e Ricardo) e outra mais de uma página (época da Regiane).
  - [ ] Verificar quantidade de arquivos de cada uma dessa épocas.
  - [ ] Verificar arquivos colocados nas seguintes páginas:
      - /media/hdvm07/bd/002/997/001/Antiga/hemeroteca-peb-metadados/arquivos-renomeados/pendencia/arquivos/ALOCAR01
      - /media/hdvm07/bd/002/997/001/Antiga/hemeroteca-peb-metadados/arquivos-renomeados/pendencia/arquivos/alocar02