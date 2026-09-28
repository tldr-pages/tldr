# base64

> Enkoduj lub dekoduj plik lub `stdin` do/z base64, do `stdout` lub innego pliku.
> Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Enkoduj plik do `stdout`:

`base64 {{[-i|--input]}} {{ścieżka/do/pliku}}`

- Enkoduj plik do określonego pliku wyjściowego:

`base64 {{[-i|--input]}} {{ścieżka/do/pliku_wejściowego}} {{[-o|--output]}} {{ścieżka/do/pliku_wyjściowego}}`

- Zawijaj zakodowane wyjście na określonej szerokości (`0` wyłącza zawijanie):

`base64 {{[-b|--break]}} {{0|76|...}} {{ścieżka/do/pliku}}`

- Dekoduj plik do `stdout`:

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{ścieżka/do/pliku}}`

- Enkoduj z `stdin` do `stdout`:

`{{komenda}} | base64`

- Dekoduj z `stdin` do `stdout`:

`{{komenda}} | base64 {{[-d|--decode]}}`
