# cp

> Copia arquivos e diretórios.
> Mais informações: <https://www.gnu.org/software/coreutils/cp>.

- Copia um arquivo para outra localização:

`cp {{caminho/para/arquivo_entrada.ext}} {{caminho/para/arquivo_saída.ext}}`

- Copia um arquivo para dentro de outro diretório, mantendo o nome:

`cp {{caminho/para/arquivo.ext}} {{caminho/para/diretório}}`

- Copia recursivamente o conteúdo de um diretório para outra localização (se o destino existe, o diretório é copiado para dentro dele):

`cp -r {{caminho/para/diretório_fonte}} {{caminho/para/diretório_alvo}}`

- Copia um diretório recursivamente, em modo verboso (mostra os arquivos conforme eles são copiados):

`cp -vr {{caminho/para/diretório_fonte}} {{caminho/para/diretório_alvo}}`

- Copia múltiplos arquivos de uma só vez para um diretório:

`cp -t {{caminho/para/diretorio_fonte}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- Copia arquivos de texto para outra localização, em modo interativo (exige confirmação do usuário antes de sobrescrever):

`cp -i {{*.txt}} {{caminho/para/diretório_alvo}}`

- Segue links simbólicos antes de copiar:

`cp -L {{link}} {{caminho/para/diretório_alvo}}`

- Usa todo o caminho dos arquivos fonte, criando quaisquer diretórios intermediários ausentes quando copia:

`cp --parents {{fonte/caminho/para/arquivo}} {{caminho/para/arquivo_alvo}}`
