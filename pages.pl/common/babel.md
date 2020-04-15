# babel

> Transpiler, który konwertuje kod ze składni JavaScript ES6 / ES7 na składnię ES5.
> Więcej informacji: <https://babeljs.io/>.

- Transpiluj określony plik wejściowy i dane wyjściowe do `stdout`:

`babel {{path/to/file}}`

- Transpiluj określony plik wejściowy i wyjście do określonego pliku:

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Transpiluj plik wejściowy przy każdej zmianie:

`babel {{path/to/input_file}} --watch`

- Transpiluj cały katalog plików:

`babel {{path/to/input_directory}}`

- Zignoruj określone pliki oddzielone przecinkami w katalogu:

`babel {{path/to/input_directory}} --ignore {{ignored_files}}`

- Transpiluj i wypisz jako zminimalizowany JavaScript:

`babel {{path/to/input_file}} --minified`

- Wybierz zestaw ustawień dla formatowania wyjściowego:

`babel {{path/to/input_file}} --presets {{presets}}`

- Wyświetl wszystkie dostępne opcje:

`babel --help`
