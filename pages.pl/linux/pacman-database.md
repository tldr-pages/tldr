# pacman --database

> Operuj na bazie danych pakietów Arch Linuksa.
> Modyfikuj niektóre atrybuty zainstalowanych pakietów.
> Zobacz także: `pacman`.
> Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Oznacz pakiet jako pośrednio zainstalowany (zależność):

`sudo pacman --database --asdeps {{nazwa_pakietu}}`

- Oznacz pakiet jako bezpośrednio zainstalowany:

`sudo pacman --database --asexplicit {{nazwa_pakietu}}`

- Sprawdź, czy wszystkie zależności pakietów są zainstalowane:

`pacman --database --check`

- Sprawdź repozytoria, aby zapewnić, że wszystkie podane zależności są dostępne:

`pacman --database --check --check`

- Wyświetlaj tylko komunikaty o błędach:

`pacman --database --check --quiet`

- Wyświetl pomoc:

`pacman --database --help`
