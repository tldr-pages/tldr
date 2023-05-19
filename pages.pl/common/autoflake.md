# autoflake

> Narzędzie do usuwania nieużywanych importów i zmiennych z kodu Python.
> Więcej informacji: <https://github.com/myint/autoflake>.

- Usuń nieużywane zmienne z jednego pliku i wyświetl różnicę:

`autoflake --remove-unused-variables {{ścieżka/do/pliku.py}}`

- Usuń nieużywane importy z wielu plików i wyświetl różnice:

`autoflake --remove-all-unused-imports {{ścieżka/do/pliku1.py ścieżka/do/pliku2.py ...}}`

- Usuń nieużywane zmienne z pliku, zastępując plik:

`autoflake --remove-unused-variables --in-place {{ścieżka/do/pliku.py}}`

- Usuń nieużywane zmienne rekurencyjnie ze wszystkich plików w katalogu, nadpisując każdy plik:

`autoflake --remove-unused-variables --in-place --recursive {{sciezka/do/katalogu}}`
