# babel

> Transpiler, który konwertuje kod ze składni JavaScript ES6/ES7 na składnię ES5.
> Więcej informacji: <https://babeljs.io/docs/babel-cli>.

- Transpiluj określony plik wejściowy i wypisz dane wyjściowe do `stdout`:

`babel {{ścieżka/do/pliku}}`

- Transpiluj określony plik wejściowy i zapisz wyjście do określonego pliku:

`babel {{ścieżka/do/pliku_wejściowego}} --out-file {{ścieżka/do/pliku_wyjściowego}}`

- Transpiluj plik wejściowy przy każdej zmianie:

`babel {{ścieżka/do/pliku_wejściowego}} --watch`

- Transpiluj cały katalog plików:

`babel {{ścieżka/do/katalogu_wejściowego}}`

- Zignoruj określone pliki oddzielone przecinkami w katalogu:

`babel {{ścieżka/do/katalogu_wejściowego}} --ignore {{ignorowany_plik1,ignorowany_plik2,...}}`

- Transpiluj i wypisz jako zminimalizowany JavaScript:

`babel {{ścieżka/do/pliku_wejściowego}} --minified`

- Wybierz zestaw ustawień dla formatowania wyjściowego:

`babel {{ścieżka/do/pliku_wejściowego}} --presets {{preset1,preset2,...}}`

- Wyświetl pomoc:

`babel --help`
