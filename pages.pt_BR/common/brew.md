# brew

> A versão Linux do gerenciador de pacotes Homebrew.
> Mais informações: <https://brew.sh>.

- Buscar por fórmulas disponíveis:

`brew search {{termo_da_busca}}`

- Instalar a última versão estável de uma fórmula (utilizar `--devel` para versões de desenvolvimento):

`brew install {{formula}}`

- Listar as fórmulas instaladas:

`brew list`

- Atualizar uma fórmula instalada (se não for informado o nome de uma fórmula, todas as fórmulas serão atualizadas):

`brew upgrade {{formula}}`

- Recuperar a versão mais recente do Linuxbrew e de todas as fórmulas do GitHub:

`brew update`

- Exibir as fórmulas que possuem novas versões disponíveis:

`brew outdated`

- Exibir informações sobre uma fórmula (versão, caminho de instalação, dependências, etc.):

`brew info {{formula}}`

- Verificar a instalação local em busca de possíveis problemas:

`brew doctor`
