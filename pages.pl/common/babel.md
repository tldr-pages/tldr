# babel

> Transpiler, który konwertuje kod ze składni JavaScript ES6 / ES7 na składnię ES5.
> Więcej informacji: <https://babeljs.io/>.

- Transpiluj określony plik wejściowy i dane wyjściowe do `stdout`:

`babel {{siezka/do/pliku}}`

- Transpiluj określony plik wejściowy i wyjście do określonego pliku:

`babel {{sciezka/do/pliku_wejsciowego}} --out-file {{sciezka/do/pliku_wyjsciowego}}`

- Transpiluj plik wejściowy przy każdej zmianie:

`babel {{sciezka/do/pliku_wejsciowego}} --watch`

- Transpiluj cały katalog plików:

`babel {{sciezka/do/katalogu_wejsciowego}}`

- Zignoruj określone pliki oddzielone przecinkami w katalogu:

`babel {{sciezka/do/katalogu_wejsciowego}} --ignore {{ignorowane_pliki}}`

- Transpiluj i wypisz jako zminimalizowany JavaScript:

`babel {{sciezka/do/pliku_wejsciowego}} --minified`

- Wybierz zestaw ustawień dla formatowania wyjściowego:

`babel {{sciezka/do/pliku_wejsciowego}} --presets {{presets}}`

- Wyświetl wszystkie dostępne opcje:

`babel --help`
