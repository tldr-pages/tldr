# pacman --deptest

> Sprawdź każdą podaną zależność i zwróć listę zależności, które nie są aktualnie spełnione.
> Zobacz także: `pacman`.
> Więcej informacji: <https://manned.org/pacman.8>.

- Wyświetl nazwy zależności, które nie są zainstalowane:

`pacman -T {{nazwa_pakietu1 nazwa_pakietu2 ...}}`

- Sprawdź, czy zainstalowany pakiet spełnia podaną minimalną wersję:

`pacman -T "{{bash>=5}}"`

- Sprawdź, czy jest zainstalowana nowsza wersja pakietu:

`pacman -T "{{bash>5}}"`

- Wyświetl pomoc:

`pacman -Th`
