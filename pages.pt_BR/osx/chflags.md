# chflags

> Altera flags de arquivo ou diretório.
> Mais informações: <https://keith.github.io/xcode-man-pages/chflags.1.html>.

- Define a flag `hidden` para um arquivo:

`chflags {{hidden}} {{caminho/para/arquivo}}`

- Remove a flag `hidden` de um arquivo:

`chflags {{nohidden}} {{caminho/para/arquivo}}`

- Define recursivamente a flag `uchg` para um diretório:

`chflags -R {{uchg}} {{caminho/para/diretório}}`

- Remove recursivamente a flag `uchg` de um diretório:

`chflags -R {{nouchg}} {{caminho/para/diretório}}`
