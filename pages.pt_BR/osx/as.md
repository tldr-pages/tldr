# as

> Montador (assembler) GNU portável.
> Principalmente destinado a montar a saída do `gcc` para ser usada pelo `ld`.
> Mais informações: <https://www.unix.com/man-page/osx/1/as/>.

- Monta (compilar) um arquivo, escrevendo a saída para `a.out`:

`as {{arquivo.s}}`

- Monta a saída para um determinado arquivo:

`as {{arquivo.s}} -o {{saida.o}}`

- Gera saída mais rapidamente ignorando espaços em branco e pré-processamento de comentários. (Só deve ser usado para compiladores confiáveis):

`as -f {{arquivo.s}}`

- Inclui um determinado caminho na lista de diretórios para pesquisar os arquivos especificados nas diretivas `.include`:

`as -I {{caminho/para/diretório}} {{arquivo.s}}`
