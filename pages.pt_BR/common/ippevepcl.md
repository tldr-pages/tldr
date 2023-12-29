# ippevepcl

> Imprime em impressoras laser HP PCL a preto e branco.
> Suporta arquivos HP PCL, PWG Raster and Apple Raster.
> Veja também: `ippevepcl`, `ippeveprinter`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Imprime um arquivo para `stdout` (mensagens de estado e progresso são enviadas para `stderr`):

`ippeveps {{caminho/para/arquivo}}`

- Imprime um arquivo de `stdin` para `stdout`:

`{{wget -O - https://examplewebsite.com/file}} | ippeveps`
