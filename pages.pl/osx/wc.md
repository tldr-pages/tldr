# wc

> Zlicza linie, słowa, i bajty
> Więcej informacji: <https://ss64.com/osx/wc.html>.

- Policz linie w pliku

`wc -l {{ścieżka/do/pliku}}`

- Policz słowa w pliku:

`wc -w {{ścieżka/do/pliku}}`

- Policz znaki (bajty) w pliku:

`wc -c {{ścieżka/do/pliku}}`

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc -m {{ścieżka/do/pliku}}`

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

`{{find .}} | wc`
