# pacman --upgrade

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`.
> Więcej informacji: <https://manned.org/pacman.8>.

- Zainstaluj jeden lub więcej pakietów z plików:

`sudo pacman -U {{ścieżka/do/pakietu1.pkg.tar.zst ścieżka/do/pakietu2.pkg.tar.zst ...}}`

- Zainstaluj pakiet bez pytania:

`sudo pacman -U --noconfirm {{ścieżka/do/pakietu.pkg.tar.zst}}`

- Nadpisz pliki będące w konflikcie podczas instalacji pakietów:

`sudo pacman -U --overwrite {{ścieżka/do/pliku}} {{ścieżka/do/pakietu.pkg.tar.zst}}`

- Zainstaluj pakiet, pomijając sprawdzanie wersji zależności:

`sudo pacman -Ud {{ścieżka/do/pakietu.pkg.tar.zst}}`

- Wyświetl pakiety, na które wpływ miałaby komenda (nie instaluje żadnych pakietów):

`pacman -Up {{ścieżka/do/pakietu.pkg.tar.zst}}`

- Wyświetl pomoc:

`pacman -Uh`
