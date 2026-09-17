# pacman --query

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`.
> Więcej informacji: <https://manned.org/pacman.8>.

- Wyświetl zainstalowane pakiety i ich wersje:

`pacman -Q`

- Wyświetl tylko pakiety niebędące zależnościami i ich wersje:

`pacman -Qe`

- Znajdź, do którego pakietu należy plik:

`pacman -Qo {{nazwa_pliku}}`

- Wyświetl informacje o zainstalowanym pakiecie:

`pacman -Qi {{nazwa_pakietu}}`

- Znajdź pliki należące do pakietu:

`pacman -Ql {{nazwa_pakietu}}`

- Wyświetl pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`pacman -Qdtq`

- Wyświetl zainstalowane pakiety, których nie ma w repozytoriach:

`pacman -Qm`

- Wyświetl przestarzałe pakiety:

`pacman -Qu`
