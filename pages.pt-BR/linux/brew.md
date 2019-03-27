# brew

> A versão Linux do gerenciador de pacotes Homebrew.

- Busca por fórmulas disponíoveis:

`brew search {{text}}`

- Instala a última versão estável de uma fórmula (utilize `--devel` para versões de desenvolvimento):

`brew install {{formula}}`

- Listar todas as fórmulas instaladas:

`brew list`

- Atualizar uma fórmula instalada (se não for informado o nome de uma fórmula, todas as fórmulas serão atualizadas):

`brew upgrade {{formula}}`

- Recupera a versão mais recente do Linuxbrew e de todas as fórmulas do Github:

`brew update`

- Exibe as fórmulas que possuem novas versões disponíveis:

`brew outdated`

- Exibe informações sobre uma fórmula (versão, caminho de instalação, dependências, etc.):

`brew info {{formula}}`

- Verifica a instalação local em busca de possíveis problemas:

`brew doctor`
