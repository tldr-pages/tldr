# pacman --database

> Operuj na bazie danych pakietów Arch Linuksa.
> Modyfikuj niektóre atrybuty zainstalowanych pakietów.
> Zobacz także: `pacman`.
> Więcej informacji: <https://manned.org/pacman.8>.

- Oznacz pakiet jako pośrednio zainstalowany (zależność):

`sudo pacman -D --asdeps {{nazwa_pakietu}}`

- Oznacz pakiet jako bezpośrednio zainstalowany:

`sudo pacman -D --asexplicit {{nazwa_pakietu}}`

- Sprawdź, czy wszystkie zależności pakietów są zainstalowane:

`pacman -Dk`

- Sprawdź repozytoria, aby zapewnić, że wszystkie podane zależności są dostępne:

`pacman -Dkk`

- Wyświetlaj tylko komunikaty o błędach:

`pacman -Dkq`

- Wyświetl pomoc:

`pacman -Dh`
