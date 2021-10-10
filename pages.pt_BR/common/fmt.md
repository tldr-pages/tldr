# fmt

> Reformata um arquivo de texto juntando seus parágrafos e limitando a largura da linha a um determinado número de caracteres (75 por padrão).
> Mais informações: <https://www.gnu.org/software/coreutils/fmt>.

- Reformata um arquivo:

`fmt {{caminho/para/arquivo}}`

- Reformata um arquivo produzindo linhas de saída de (no máximo) `n` caracteres:

`fmt -w {{n}} {{caminho/para/arquivo}}`

- Reformata um arquivo sem unir linhas menores do que a largura fornecida:

`fmt -s {{caminho/para/arquivo}}`

- Reformata um arquivo com espaçamento uniforme (1 espaço entre palavras e 2 espaços entre parágrafos):

`fmt -u {{caminho/para/arquivo}}`
