# cp

> Copia arquivos e diretórios.
> Mais informações: <https://www.gnu.org/software/coreutils/cp>.

- Copia um arquivo para outra locação:

`cp {{caminho/para/arquivo_origem.ext}} {{caminho/para/arquivo_destino.ext}}`

- Copia um arquivo para outro diretório, mantendo o mesmo nome:

`cp {{caminho/para/arquivo_origem.ext}} {{caminho/para/diretorio_pai_destino}}`

- Copia recursivamente o conteúdo de um diretório para outra locação (se a locação de destino existe, o diretório é copiado dentro dele):

`cp -R {{caminho/para/diretorio_origem}} {{caminho/para/diretorio_destino}}`

- Copia um diretório recursivamente, em modo verboso (mostra arquivos que estão sendo copiados):

`cp -vR {{caminho/para/diretorio_origem}} {{caminho/para/diretorio_destino}}`

- Copia arquivos de texto para outra locação, em modo interativo (pergunta ao usuário antes de sobrescrever):

`cp -i {{*.txt}} {{caminho/para/diretorio_destino}}`

- Segue links simbólicos antes de realizar a cópia:

`cp -L {{link}} {{caminho/para/diretorio_destino}}`
