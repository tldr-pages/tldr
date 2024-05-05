# prstat

> Raportuj statystyki aktywnego procesu.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Sprawdź wszystkie procesy i raportuj statystyki posortowane według użycia procesora:

`prstat`

- Sprawdź wszystkie procesy i raportuj statystyki posortowane według użycia pamięci:

`prstat -s rss`

- Raportuj podsumowanie całkowitego użycia dla każdego użytkownika:

`prstat -t`

- Raportuj informacje o pomiarach procesu mikrostanu:

`prstat -m`

- Wypisz 5 najbardziej obciążających procesor procesów co sekundę:

`prstat -c -n {{5}} -s cpu {{1}}`
