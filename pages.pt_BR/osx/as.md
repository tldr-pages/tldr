# as

> Montador (assembler) GNU portável.
> Principalmente destinado a montar a saída do `gcc` para ser usada pelo `ld`.
> Mais informações: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Monta (compilar) um arquivo, escrevendo a saída para `a.out`:

`as {{caminho/para/arquivo.s}}`

- Monta a saída para um determinado arquivo:

`as {{caminho/para/arquivo.s}} -o {{caminho/para/saida.o}}`

- Gera saída mais rapidamente ignorando espaços em branco e pré-processamento de comentários. (Só deve ser usado para compiladores confiáveis):

`as -f {{caminho/para/arquivo.s}}`

- Inclui um determinado caminho na lista de diretórios para pesquisar os arquivos especificados nas diretivas `.include`:

`as -I {{caminho/para/diretório}} {{caminho/para/arquivo.s}}`
