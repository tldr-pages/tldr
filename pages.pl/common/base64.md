# base64

> Enkoduj lub dekoduj plik lub standardowe wejście do/z Base64, na standardowe wyjście.
> Więcej informacji: <https://manned.org/base64>.

- Enkoduj plik:

`base64 {{ścieżka/do/pliku}}`

- Zawijaj zakodowane wyjście na określonej szerokości (`0` wyłącza zawijanie):

`base64 {{[-w|--wrap]}} {{0|76|...}} {{ścieżka/do/pliku}}`

- Dekoduj plik:

`base64 {{[-d|--decode]}} {{ścieżka/do/pliku}}`

- Enkoduj z `stdin`:

`{{jakiespolecenie}} | base64`

- Dekoduj z `stdin`:

`{{jakiespolecenie}} | base64 {{[-d|--decode]}}`
