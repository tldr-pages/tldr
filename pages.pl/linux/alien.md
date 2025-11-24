# alien

> Konwertuj różne pakiety instalacyjne na inne formaty.
> Więcej informacji: <https://manned.org/alien>.

- Konwertuj wskazany plik instalacyjny do formatu Debiana (rozszerzenie `.deb`):

`sudo alien {{[-d|--to-deb]}} {{ścieżka/do/pliku}}`

- Konwertuj wskazany plik instalacyjny do formatu Red Hata (rozszerzenie `.rpm`):

`sudo alien {{[-r|--to-rpm]}} {{ścieżka/do/pliku}}`

- Konwertuj wskazany plik instalacyjny do formatu plików instalacyjnych Slackware (rozszerzenie `.tgz`):

`sudo alien {{[-t|--to-tgz]}} {{ścieżka/do/pliku}}`

- Konwertuj wskazany plik instalacyjny do formatu Debiana i zainstaluj go w systemie:

`sudo alien {{[-d|--to-deb]}} --install {{ścieżka/do/pliku}}`
