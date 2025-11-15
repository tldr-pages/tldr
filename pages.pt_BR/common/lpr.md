# lpr

> Ferramenta do CUPS para imprimir arquivos.
> Veja também: `lpstat`, `lpadmin`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-lpr.html>.

- Imprime um arquivo na impressora padrão:

`lpr {{caminho/para/arquivo}}`

- Imprime 2 cópias:

`lpr -# {{2}} {{caminho/para/arquivo}}`

- Imprime em uma impressora específica:

`lpr -P {{impressora}} {{caminho/para/arquivo}}`

- Imprime uma única página (p. ex., 2) ou uma faixa de páginas (p. ex., 2-16):

`lpr -o page-ranges={{2|2-16}} {{caminho/para/arquivo}}`

- Imprime frente e verso em modo retrato (long) ou paisagem (short):

`lpr -o sides={{two-sided-long-edge|two-sided-short-edge}} {{caminho/para/arquivo}}`

- Define o tamanho da página (mais opções podem estar disponíveis dependendo da configuração):

`lpr -o media={{a4|letter|legal}} {{caminho/para/arquivo}}`

- Imprime múltiplas páginas por folha:

`lpr -o number-up={{2|4|6|9|16}} {{caminho/para/arquivo}}`
