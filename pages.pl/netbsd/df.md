# df

> Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików.
> Więcej informacji: <https://man.netbsd.org/df.1>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Użyj jednostek czytelnych dla człowieka (z ang. [h]uman) (opartych na potęgach 1024):

`df -h`

- Wyświetl wszystkie pola struktury/struktur zwróconych przez `statvfs`:

`df -G`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df {{ścieżka/do/pliku_lub_katalogu}}`

- Dołącz statystyki dotyczące liczby wolnych i wykorzystanych [i]węzłów:

`df -i`

- Użyj jednostek 1024-bajtowych do wyświetlania danych o przestrzeni dyskowej:

`df -k`

- Wyświetl informację w sposób [P]rzenośny:

`df -P`
