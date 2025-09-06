# 7zr

> Archiwizator plików o wysokim współczynniku kompresji.
> Podobny do `7z` z wyjątkiem tego, że obsługuje tylko pliki `7z`.
> Więcej informacji: <https://manned.org/7zr>.

- Z[a]rchiwizuj plik lub katalog:

`7zr a {{ścieżka/do/archiwum.7z}} {{ścieżka/do/pliku_lub_katalogu}}`

- Zaszyfruj istniejące archiwum (w tym nazwy plików):

`7zr a {{ścieżka/do/zaszyfrowanego.7z}} -p{{hasło}} -mhe={{on}} {{ścieżka/do/archiwum.7z}}`

- Wypakuj archiwum, zachowując oryginalną strukturę katalogów:

`7zr x {{ścieżka/do/archiwum.7z}}`

- Wypakuj archiwum do określonego katalogu:

`7zr x {{ścieżka/do/archiwum.7z}} -o{{ścieżka/do/wyjścia}}`

- Wypakuj archiwum do `stdout`:

`7zr x {{ścieżka/do/archiwum.7z}} -so`

- Wypisz zawartość pliku archiwum:

`7zr l {{ścieżka/do/archiwum.7z}}`

- Ustaw poziom kompresji (wyższy oznacza wyższą kompresję, ale wolniejszą):

`7zr a {{ścieżka/do/archiwum.7z}} -mx={{0|1|3|5|7|9}} {{ścieżka/do/pliku_lub_katalogu}}`
