# 7za

> Archiwizator plików o wysokim współczynniku kompresji.
> Podobny do `7z` z wyjątkiem tego, że obsługuje mniej typów plików, ale jest wieloplatformowy.
> Więcej informacji: <https://manned.org/7za>.

- Zarchiwizuj plik lub katalog:

`7za a {{ścieżka/do/archiwum.7z}} {{ścieżka/do/pliku_lub_katalogu}}`

- Zaszyfruj istniejące archiwum (w tym nagłówki):

`7z a {{ścieżka/do/zaszyfrowanego.7z}} -p{{hasło}} -mhe=on {{ścieżka/do/archiwum.7z}}`

- Wyodrębnij istniejący plik 7z z oryginalną strukturą katalogów:

`7za x {{ścieżka/do/archiwum.7z}}`

- Wyodrębnij archiwum do określonego katalogu:

`7z x {{ścieżka/do/archiwum.7z}} -o{{ścieżka/do/wyjścia}}`

- Wypakuj archiwum do `stdout`:

`7z x {{ścieżka/do/archiwum.7z}} -so`

- Zarchiwizuj przy użyciu określonego typu archiwum:

`7z a -t{{7z|bzip2|gzip|lzip|tar|...}} {{ścieżka/do/archiwum.7z}} {{ścieżka/do/pliku_lub_katalogu}}`

- Wypisz zawartość pliku archiwum:

`7z l {{ścieżka/do/archiwum.7z}}`
