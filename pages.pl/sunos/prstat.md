# prstat

> Raportowanie statystyk aktywnego procesu.
> Więcej informacji: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Sprawdzenie wszystkich procesów i raportowanie statystyk posortowanych według użycia procesora:

`prstat`

- Sprawdzenie wszystkich procesów i raportowanie statystyk posortowanych według użycia pamięci:

`prstat -s rss`

- Raportowanie podsumowania całkowitego użycia dla każdego użytkownika:

`prstat -t`

- Raportowanie informacji o pomiarach procesu mikrostanu:

`prstat -m`

- Wypisywanie listy 5 najbardziej obciążających procesor procesów co sekundę:

`prstat -c -n {{5}} -s cpu {{1}}`
