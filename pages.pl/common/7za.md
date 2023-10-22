# 7za

> Archiwizator plików o wysokim współczynniku kompresji.
> Samodzielna wersja `7z` z obsługą mniejszej liczby typów archiwów.
> Więcej informacji: <https://manned.org/7za>.

- Zarchiwizuj plik lub katalog:

`7za a {{archiwum.7z}} {{scieżka/do/pliku_lub_katalogu}}`

- Wyodrębnij istniejący plik 7z z oryginalną strukturą katalogów:

`7za x {{archiwum}}`

- Zarchiwizuj przy użyciu określonego typu archiwum:

`7za a -t{{zip|gzip|bzip2|tar}} {{archiwum}} {{scieżka/do/pliku_lub_katalogu}}`

- Wypisz dostępe typy archiwów:

`7za i`

- Wypisz zawartość pliku archiwum:

`7za l {{archiwum}}`
