# df

> Wyświetl przegląd wykorzystania przestrzeni dyskowej systemu plików.
> Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?df>.

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków w jednostkach 512-bajtowych:

`df`

- Użyj jednostek czytelnych dla człowieka (z ang. [h]uman) (opartych na potęgach 1024) i wyświetl sumę całkowitą:

`df -h -c`

- Użyj jednostek czytelnych dla człowieka (z ang. [H]uman) (opartych na potęgach 1000):

`df -{{-si|H}}`

- Wyświetl wszystkie systemy plików i ich wykorzystanie dysków zawierające podany plik lub katalog:

`df {{ścieżka/do/pliku_lub_katalogu}}`

- Dołącz statystyki dotyczące liczby wolnych i wykorzystanych [i]-węzłów wraz z [T]ypami systemów plików:

`df -iT`

- Użyj jednostek 1024-bajtowych do wyświetlania danych o przestrzeni dyskowej:

`df -k`

- Wyświetl informację w sposób [P]rzenośny:

`df -P`
