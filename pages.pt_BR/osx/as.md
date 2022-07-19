# as

> Montador (assembler) GNU portável.
> Principalmente destinado a montar a saída do `gcc` para ser usada pelo `ld`.
> Mais informações: <https://www.unix.com/man-page/osx/1/as/>.

- Montar (compilar) um arquivo, escrevendo a saída para `a.out`:

`as {{arquivo.s}}`

- Montar a saída para um determinado arquivo:

`as {{arquivo.s}} -o {{saida.o}}`

- Gerar saída mais rapidamente ignorando espaços em branco e pré-processamento de comentários. (Só deve ser usado para compiladores confiáveis)

`as -f {{arquivo.s}}`

- Incluir um determinado caminho na lista de diretórios para pesquisar os arquivos especificados nas diretivas `.include`:

`as -I {{caminho/para/diretório}} {{arquivo.s}}`
