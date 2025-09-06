# ncdu

> Analisador de uso de disco com uma interface ncurses.
> Mais informações: <https://manned.org/ncdu>.

- Analisa o diretório de trabalho atual:

`ncdu`

- Colore a saída:

`ncdu --color {{dark|off}}`

- Analisa um dado diretório:

`ncdu {{caminho/para/diretório}}`

- Salva os resultados em um arquivo:

`ncdu -o {{caminho/para/arquivo}}`

- Exclui arquivos que correspondem a um padrão, o argumento pode ser fornecido várias vezes para adicionar mais padrões:

`ncdu --exclude '{{*.txt}}'`
