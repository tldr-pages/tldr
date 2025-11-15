# 7za

> Archiwizator plików o wysokim współczynniku kompresji.
> Podobny do `7z` z wyjątkiem tego, że obsługuje mniej typów plików, ale jest wieloplatformowy.
> Więcej informacji: <https://manned.org/7za>.

- Z[a]rchiwizuj plik lub katalog:

`7za a {{ścieżka/do/archiwum.7z}} {{ścieżka/do/pliku_lub_katalogu}}`

- Zaszyfruj istniejące archiwum (w tym nazwy plików):

`7za a {{ścieżka/do/zaszyfrowanego.7z}} -p{{hasło}} -mhe={{on}} {{ścieżka/do/archiwum.7z}}`

- Wypakuj archiwum, zachowując oryginalną strukturę katalogów:

`7za x {{ścieżka/do/archiwum.7z}}`

- Wypakuj archiwum do określonego katalogu:

`7za x {{ścieżka/do/archiwum.7z}} -o{{ścieżka/do/wyjścia}}`

- Wypakuj archiwum do `stdout`:

`7za x {{ścieżka/do/archiwum.7z}} -so`

- Zarchiwizuj przy użyciu określonego typu archiwum:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{ścieżka/do/archiwum.7z}} {{ścieżka/do/pliku_lub_katalogu}}`

- Wypisz zawartość pliku archiwum:

`7za l {{ścieżka/do/archiwum.7z}}`

- Ustaw poziom kompresji (wyższy oznacza wyższą kompresję, ale wolniejszą):

`7za a {{ścieżka/do/archiwum.7z}} -mx={{0|1|3|5|7|9}} {{ścieżka/do/pliku_lub_katalogu}}`
