# Hemeroteca de Política Externa Brasileira


- [Informações sobre o projeto](https://apoio.labriunesp.org/docs/projetos/dados/hemeroteca-peb/intro)


```
conda config --set pip_interop_enabled True
conda config --set env_prompt '({name})'
conda config --add envs_dirs ./env
touch environment.yml && conda env create -f environment.yml
git pull origin main && conda activate env_hemeroteca-peb
conda env update --prune
```

## Etapas

- [x] Acesso a estação remota de trabalho

- [x] Terminal e Comando Básicos Linux

- [x] Editor de códio (VsCode)

- [x] Versionamento (Git/GitLab)

- [x] Ambiente Virtual (anaconda)

- [x] Fundamentos de Programação (Python)

- [x] Nomeação dos arquivos pendentes da Hemeroteca

- [ ] OCR nos arquivos (gerar pdf pesquisável)
  - [ ] ocrmypdf
  - [ ] layoutparser
  - [ ] OpenCV/Pillow
    - [Deep Learning based Super Resolution with OpenCV](https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066)
    - [OpenCV Super Resolution with Deep Learning](https://www.pyimagesearch.com/2020/11/09/opencv-super-resolution-with-deep-learning/)

- [ ] Inserção de metadados a partir no nome dos arquivos

- [ ] substituir arquivos da hemeroteca

- [ ] Analise de dados (pandas)

- [ ] buscar substituir arquivos pdf por html

- [ ] aprendizado de máquina
