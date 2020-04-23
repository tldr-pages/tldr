# autoflake

> Narzędzie do usuwania nieużywanych importów i zmiennych z kodu Python.
> Więcej informacji: <https://github.com/myint/autoflake>.

- Usuń nieużywane zmienne z jednego pliku i wyświetl różnicę:

`autoflake --remove-unused-variables {{file.py}}`

- Usuń nieużywane importy z wielu plików i wyświetl różnice:

`autoflake --remove-all-unused-imports {{file1.py}} {{file2.py}} {{file3.py}}`

- Usuń nieużywane zmienne z pliku, zastępując plik:

`autoflake --remove-unused-variables --in-place {{file.py}}`

- Usuń nieużywane zmienne rekurencyjnie ze wszystkich plików w katalogu, nadpisując każdy plik:

`autoflake --remove-unused-variables --in-place --recursive {{sciezka/do/katalogu}}`
