# chflags

> Altera flags de arquivo ou diretório.
> Mais informações: <https://ss64.com/osx/chflags.html>.

- Definir a flag `hidden` para um arquivo:

`chflags {{hidden}} {{caminho/para/arquivo}}`

- Remover a flag `hidden` de um arquivo:

`chflags {{nohidden}} {{caminho/para/arquivo}}`

- Definir recursivamente a flag `uchg` para um diretório:

`chflags -R {{uchg}} {{caminho/para/diretório}}`

- Remover recursivamente a flag `uchg` de um diretório:

`chflags -R {{nouchg}} {{caminho/para/diretório}}`
