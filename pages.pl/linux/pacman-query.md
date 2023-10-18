# pacman --query

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`.
> Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Wyświetl zainstalowane pakiety i ich wersje:

`pacman --query`

- Wyświetl tylko pakiety niebędące zależnościami i ich wersje:

`pacman --query --explicit`

- Znajdź, do którego pakietu należy plik:

`pacman --query --owns {{nazwa_pliku}}`

- Wyświetl informacje o zainstalowanym pakiecie:

`pacman --query --info {{nazwa_pakietu}}`

- Znajdź pliki należące do pakietu:

`pacman --query --list {{nazwa_pakietu}}`

- Wyświetl pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`pacman --query --unrequired --deps --quiet`

- Wyświetl zainstalowane pakiety, których nie ma w repozytoriach:

`pacman --query --foreign`

- Wyświetl przestarzałe pakiety:

`pacman --query --upgrades`
