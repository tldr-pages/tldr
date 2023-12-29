# cupsenable

> Inicia impressoras e classes.
> NOTA: destino se refere a uma impressora ou uma classe de impressoras.
> Veja também: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- Inicia um ou mais destino(s):

`cupsenable {{destino1 destino2 ...}}`

- Resume a impressão de trabalhos pendentes de um destino (use após `cupsdisable` com `--hold`):

`cupsenable --release {{destination}}`

- Cancela todos os trabalhos do(s) destino(s) especificado(s):

`cupsenable -c {{destination1 destination2 ...}}`
