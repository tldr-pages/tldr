# cupsenable

> Inicia impressoras e classes.
> Veja também: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
> Mais informações: <https://www.cups.org/doc/man-cupsenable.html>.

- Inicia um ou mais destino(s):

`cupsenable {{destino1 destino2 ...}}`

- Resumir impressão de trabalhos pendentes de um destino (usar depois de `cupsdisable` com `--hold`):

`cupsenable --release {{destino}}`

- Cancelar todos os trabalhos dos destinos especificados:

`cupsenable -c {{destino1 destino2 ...}}`
