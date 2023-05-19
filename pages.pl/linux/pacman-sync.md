# pacman --sync

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`.
> Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Zainstaluj nowy pakiet:

`sudo pacman -S {{nazwa_pakietu}}`

- Zsynchronizuj i zaktualizuj wszystkie pakiety (użyj `--downloadonly` aby pobrać pakiety i ich nie zaktualizować):

`sudo pacman --sync --refresh --sysupgrade`

- Zaktualizuj wszystkie pakiety i zainstaluj nowy bez pytania:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{nazwa_pakietu}}`

- Przeszukaj bazę danych pakietów używając wyrażenia regularnego lub słowa klucz:

`pacman -Ss "{{zapytanie}}"`

- Wyświetl informacje o pakiecie:

`pacman --sync --info {{nazwa_pakietu}}`

- Nadpisz pliki będące w konflikcie podczas aktualizacji pakietów:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{ścieżka/do/pliku}}`

- Zsynchronizuj i zaktualizuj wszystkie pakiety, ale zignoruj konkretny pakiet (można użyć więcej niż raz):

`sudo pacman --sync --refresh --sysupgrade --ignore {{nazwa_pakietu}}`

- Usuń niezainstalowane pakiety i nieużywane repozytoria z pamięci podręcznej (użyj dwa razy opcji `--clean`, aby wyczyścić wszystkie pakiety):

`sudo pacman --sync --clean`
