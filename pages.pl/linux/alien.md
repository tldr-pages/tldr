# alien

> Konwertuje różne pakiety instalacyjne na inne formaty.
> Więcej informacji: <https://manned.org/alien>.

- Konwertuj wskazany plik instalacyjny do formatu Debiana (rozszerenie `.deb`):

`sudo alien --to-deb {{ścieżka/do/pliku}}`

- Konwertuj wskazany plik instalacyjny do formatu Red Hata (rozszerzenie `.rpm`):

`sudo alien --to-rpm {{ścieżka/do/pliku}`

- Konwertuj wskazany plik instalacyjny do formatu plików instalacyjnych Slackware (rozszerzenie `.tgz`):

`sudo alien --to-tgz {{ścieżka/do/pliku}}`

- Konwertuj wskazany plik instalacyjny do formatu Debiana i zainstaluj go w systemie:

`sudo alien --to-deb --install {{ścieżka/do/pliku}}`
