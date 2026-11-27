# wc

> Zlicza linie, słowa, i bajty.
> Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Policz linie w pliku:

`wc {{[-l|--lines]}} {{ścieżka/do/pliku}}`

- Policz słowa w pliku:

`wc {{[-w|--words]}} {{ścieżka/do/pliku}}`

- Policz znaki (bajty) w pliku:

`wc {{[-c|--bytes]}} {{ścieżka/do/pliku}}`

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc {{[-m|--chars]}} {{ścieżka/do/pliku}}`

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

`{{find .}} | wc`

- Policz długość najdłuższej linii w pliku:

`wc {{[-L|--max-line-length]}} {{ścieżka/do/pliku}}`
