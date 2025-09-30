# base32

> Enkoduj lub dekoduj plik lub standardowe wejście do/z Base32, na standardowe wyjście.
> Więcej informacji: <https://manned.org/base32>.

- Enkoduj plik:

`base32 {{ścieżka/do/pliku}}`

- Zawijaj zakodowane wyjście do określonej szerokości (`0` wyłącza zawijanie):

`base32 {{[-w|--wrap]}} {{0|76|...}} {{ścieżka/do/pliku}}`

- Dekoduj plik:

`base32 {{[-d|--decode]}} {{ścieżka/do/pliku}}`

- Enkoduj z `stdin`:

`{{jakiespolecenie}} | base32`

- Dekoduj z `stdin`:

`{{jakiespolecenie}} | base32 {{[-d|--decode]}}`
