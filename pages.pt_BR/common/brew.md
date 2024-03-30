# brew

> A versão Linux do gerenciador de pacotes Homebrew.
> Mais informações: <https://docs.brew.sh/Manpage>.

- Instala a última versão estável de uma fórmula (utilizar `--devel` para versões de desenvolvimento):

`brew install {{formula}}`

- Lista as fórmulas instaladas:

`brew list`

- Atualiza uma fórmula instalada (se não for informado o nome de uma fórmula, todas as fórmulas serão atualizadas):

`brew upgrade {{formula}}`

- Recupera a versão mais recente do Linuxbrew e de todas as fórmulas do GitHub:

`brew update`

- Exibe as fórmulas que possuem novas versões disponíveis:

`brew outdated`

- Busca por fórmulas disponíveis:

`brew search {{termo_da_busca}}`

- Exibe informações sobre uma fórmula (versão, caminho de instalação, dependências, etc.):

`brew info {{formula}}`

- Verifica a instalação local em busca de possíveis problemas:

`brew doctor`
