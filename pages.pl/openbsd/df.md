# df

> Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików.
> Więcej informacji: <https://man.openbsd.org/df.1>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w formie czytelnej dla człowieka (w oparciu o potęgi 1024):

`df -h`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df {{ścieżka/do/pliku_lub_folderu}}`

- Wyświetl statystyki dotyczące liczby wolnych i wykorzystanych [i]-węzłów:

`df -i`

- Użyj jednostek 1024-bajtowych do zapisu danych przestrzennych:

`df -k`

- Wyświetl informację w [P]rzenośny sposób:

`df -P`
