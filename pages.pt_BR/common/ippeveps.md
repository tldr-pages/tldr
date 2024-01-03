# ippeveps

> Imprime em impressoras Adobe PostScript.
> Suporta arquivos PDF, PostScript, JPEG, PWG Raster or Apple Raster.
> Veja também: `ippevepcl`, `ippeveprinter`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>.

- Imprime um arquivo para `stdout` (mensagens de estado e progresso são enviadas para `stderr`):

`ippeveps {{caminho/para/arquivo}}`

- Imprime um arquivo de `stdin` para `stdout`:

`{{wget -O - https://examplewebsite.com/file}} | ippeveps`
