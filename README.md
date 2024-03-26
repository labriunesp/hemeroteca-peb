[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10884093.svg)](https://doi.org/10.5281/zenodo.10884093)

[![](<https://img.shields.io/badge/Dataverse DOI-10.7910/DVN/V3S58Q-orange>)](https://www.doi.org/10.7910/DVN/V3S58Q)

# Hemeroteca de Política Externa Brasileira

<div align="center">
<img src="https://labriunesp.org/img/hemeroteca-peb/hemeroteca-logo.svg" />

</div>

-----

<div align="center">

[![Static Badge](https://img.shields.io/badge/hemerotecapeb-apresenta%C3%A7%C3%A3o-%2303223f)](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/info) [![Static Badge](https://img.shields.io/badge/hemerotecapeb-equipe-%2303223f)](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/equipe) [![Static Badge](https://img.shields.io/badge/hemerotecapeb-atividades-%2303223f)](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/atividades) [![Static Badge](https://img.shields.io/badge/hemerotecapeb-documenta%C3%A7%C3%A3o-%2303223f)](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/infos/projetos/dados/hemeroteca-peb/infos/intro) [![Static Badge](https://img.shields.io/badge/hemerotecapeb-citar-%2303223f)](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/projetos/dados/hemeroteca-peb/citar)

</div>

A **Hemeroteca de Política Externa Brasileira** contém uma seleção de matérias publicadas, no período de 1972 a 2010, por alguns jornais brasileiros dentre os quais se destacam: O Estado de S. Paulo, Folha de S. Paulo e Gazeta Mercantil. O objetivo desta Hemeroteca é permitir aos pesquisadores interessados o acesso a notícias que foram selecionadas e classificadas ao longo dos anos, de 1972 até 2010, sobre importantes acontecimentos atinentes às relações internacionais do Brasil.

-----

Para acessar o **acervo** da Hemeroteca PEB, [clique aqui](https://hemerotecapeb.lantri.org/recoll/).

Para **mais informações** sobre o projeto, [clique aqui](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/info).

Acesse o site do **[LabRI/UNESP](https://labriunesp.org/)** e saiba mais sobre o nosso *Hub* Acadêmico.

Acesse as tarefas do treinamento [clique aqui](https://gitlab.com/unesp-labri/projeto/hemeroteca-peb/-/boards?label_name[]=treinamento&label_name[]=turma-01)

## Equipe

Conheça a equipe de [coordenadores](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/equipe#coordernadores-do-projeto) e 
[colaboradores](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/equipe#colaboradores-do-projeto) da Hemeroteca PEB.

## Versionamento

Se essa é a primeira vez que você irá baixar/clonar esse repositório, veja as instruções indicadas nesta [página](https://labriunesp.org/docs/projetos/sistemas/cadernos/versionamento).

Caso já tenha baixado/clonado esse repositório os comandos abaixo são usualmente utilizados para versionar e sincronizar o seu repositório local com o remoto.

### ETAPA 01: Gravando mudanças

Utilize o seguinte comando para gravar modificações feitas no código:

``` git add . && git commit -m 'inserir mensagem' ```

**Onde:**

`git add .` adiciona as últimas mudanças nos conteúdos do diretório atual (referida como `.`) à lista de mudanças a serem gravadas no repositório. Deve ser efetuado sempre que novas mudanças são feitas.

`&&` encadeia comandos para que sejam executados sequencialmente.

`git commit` "comete" as mudanças feitas nos arquivos monitorados, gravando-as no repositório.

`-m 'mensagem'` especifica mensagem que descreva as mudanças. A descrição deve estar entre aspas simples ou duplas.

### ETAPA 02: Sincronizando o repositório

Ao usar os comandos acima, as mudanças são salvas (gravadas) apenas na sua máquina local.

É necessário sincronizar o repositório local com o repositório remoto, o que é feito através dos seguinte comando:

```git pull origin main && git push origin main```

**Onde:**

`git pull origin main` sincroniza todos os commits mais recentes do repositório remoto e os integra no repositório local.

`git push origin main` envia as alterações do repositório local para o repositório remoto 

 o `origin main` são argumentos para especificar que a origem dos commits a serem integrados é o ramo `main` do repositório remoto. Estes argumentos não são mandatório, no entanto, explicitá-los garante que não hajam conflitos.

 - É importante que qualquer mudança no repositório seja salva/gravada (ver etapa 01) antes da sincronização com o repositório remoto (etapa 02). 
 - Recomendamos que o `git pull` sempre ser executado antes de `git push` para evitar conflitos ao mesclar as modificações do repositório local com o remoto.

## Ambiente Virtual

Para informações de configuração do ambiente virtual, [clique aqui](https://labriunesp.org/docs/projetos/sistemas/cadernos/ambiente-virtual).

### Etapa 01: Abrir o terminal


<div align="center">
  <img src="https://i.imgur.com/e7BPvav.gif" width="650" />
</div>


### Etapa 02: Abrir a pasta onde está o repositório 


<div align="center">
  <img src="https://i.imgur.com/3jlXsFO.gif" width="650" />
</div>

### Etapa 03: Ativar o ambiente virtual

Vá a raiz do repositório. Em geral, a raiz do repositório é a pasta com o nome do projeto, nesse caso `hemeroteca-peb`. A partir dessa pasta, ative o ambiente a partir do seguinte comando:

``` conda activate env_hemeroteca-peb ```

<div align="center">
  <img src="https://i.imgur.com/c0RzCmw.gif" width="650" />
</div>


## Atividades

- [Realizadas](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/atividades#atividades-realizadas)

- [Programadas](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/atividades#próximas-atividades)

## Documentação

Acesse a documentação do projeto Hemeroteca PEB clicando [aqui](https://labriunesp.org/docs/projetos/dados/hemeroteca-peb/infos/intro).
