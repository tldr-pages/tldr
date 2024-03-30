# pacman

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Odpowiednie polecenia dla innych menedżerów pakietów: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Zsynchronizuj i zaktualizuj wszystkie pakiety:

`sudo pacman -Syu`

- Zainstaluj nowy pakiet:

`sudo pacman -S {{pakiet}}`

- Usuń pakiet i jego zależności:

`sudo pacman -Rs {{pakiet}}`

- Poszukaj w bazie danych pakietów zawierających podany plik:

`pacman -F "{{nazwa_pliku}}"`

- Wyświetl zainstalowane pakiety i ich wersje:

`pacman -Q`

- Wyświetl tylko pakiety niebędące zależnościami i ich wersje:

`pacman -Qe`

- Wyświetl pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`pacman -Qtdq`

- Wyczyść całą pamięć podręczną pacmana:

`sudo pacman -Scc`
