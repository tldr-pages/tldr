# wc

> Zlicza linie, słowa, i bajty
> Więcej informacji: <https://www.gnu.org/software/coreutils/wc>.

- Policz linie w pliku

`wc -l {{plik}}`

- Policz słowa w pliku:

`wc -w {{plik}}`

- Policz znaki (bajty) w pliku:

`wc -c {{plik}}`

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc -m {{plik}}`

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

`{{find .}} | wc`

- Policz długość najdłuższej linii w pliku:

`wc --max-line-length {{plik}}`
