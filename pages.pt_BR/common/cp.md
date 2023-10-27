# cp

> Copia arquivos e diretórios.
> Mais informações: <https://www.gnu.org/software/coreutils/cp>.

- Copia um arquivo para outra localização:

`cp {{caminho/para/arquivo_origem.ext}} {{caminho/para/arquivo_destino.ext}}`

- Copia um arquivo em outro diretório, mantendo o nome do arquivo:

`cp {{caminho/para/arquivo_origem.ext}} {{caminho/para/diretório_pai_destino}}`

- Copia recursivamente o conteúdo de um diretório para outra localização (se o destino existe, o diretório é copiado dentro dele):

`cp -R {{caminho/para/diretório_origem}} {{caminho/para/diretório_destino}}`

- Copia um diretório recursivamente, em modo verboso (mostra arquivos que estão sendo copiados):

`cp -vR {{caminho/para/diretório_origem}} {{caminho/para/diretório_destino}}`

- Copia múltiplos arquivos de uma só vez para um diretório:

`cp -t {{caminho/para/diretório_destino}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- Copia arquivos de texto para outra localização, em modo interativo (pergunta ao usuário antes de sobrescrever):

`cp -i {{*.txt}} {{caminho/para/diretório_destino}}`

- Segue links simbólicos antes de copiar:

`cp -L {{link}} {{caminho/para/diretório_destino}}`

- Usa o primeiro argumento como o diretório destino (útil para `xargs ... | cp -t <DIR_DEST>`):

`cp -t {{caminho/para/diretório_destino}} {{caminho/para/arquivo_ou_diretório1 caminho/para/arquivo_ou_diretório2 ...}}`
