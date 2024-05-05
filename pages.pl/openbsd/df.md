# df

> Wyświetlanie przeglądu wykorzystania przestrzeni dyskowej systemu plików.
> Więcej informacji: <https://man.openbsd.org/df.1>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w formie czytelnej dla człowieka (w oparciu o potęgi 1024):

`df -h`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df {{sciezka/do/pliku_lub_folderu}}`

- Zawiera statystyki dotyczące liczby wolnych i wykorzystanych [i]-węzłów:

`df -i`

- Do zapisu danych przestrzennych użyj jednostek 1024-bajtowych:

`df -k`

- Wyświetlanie informacji w [P]rzenośny sposób:

`df -P`
