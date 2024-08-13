# grep

> Acha padrões em arquivos usando expressões regulares.
> Mais informações: <https://www.gnu.org/software/grep/manual/grep.html>.

- Pesquisa por um padrão em um arquivo:

`grep "{{padrão_pesquisado}}" {{caminho/para/arquivo}}`

- Pesquisa por uma string exata (desabilita expressões regulares):

`grep {{-F|--fixed-strings}} "{{string_exata}}" {{caminho/para/arquivo}}`

- Pesquisa por um padrão em todos os arquivos recursivamente em um diretório, mostrando o número das linhas das correspondências, ignorando arquivos binários:

`grep {{-r|--recursive}} {{-n|--line-number}} --binary-files={{without-match}} "{{padrão_pesquisado}}" {{caminho/para/diretório}}`

- Usa expressões regulares estendidas (suporta `?`, `+`, `{}`, `()` and `|`), no modo insensível a maiúsculas e minúsculas:

`grep {{-E|--extended-regexp}} {{-i|--ignore-case}} "{{padrão_pesquisado}}" {{caminho/para/arquivo}}`

- Imprime 3 linhas de contexto em volta, antes ou depois de cada correspondência:

`grep --{{context|before-context|after-context}} 3 "{{padrão_pesquisado}}" {{caminho/para/arquivo}}`

- Imprime o nome do arquivo e o número da linha para cada correspondência:

`grep {{-H|--with-filename}} {{-n|--line-number}} --color=always "{{padrão_pesquisado}}" {{caminho/para/arquivo}}`

- Pesquisa por linhas que correspondem a um padrão, imprimindo apenas o texto correspondido:

`grep {{-o|--only-matching}} "{{padrão_pesquisado}}" {{caminho/para/arquivo}}`

- Pesquisa `stdin` para linhas que não correspondem a um padrão:

`cat {{caminho/para/arquivo}} | grep {{-v|--invert-match}} "{{padrão_pesquisado}}"`
