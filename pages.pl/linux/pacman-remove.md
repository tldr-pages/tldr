# pacman --remove

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`.
> Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Usuń pakiet i jego zależności:

`sudo pacman --remove --recursive {{nazwa_pakietu}}`

- Usuń pakiet, jego zależności i pliki konfiguracyjne:

`sudo pacman --remove --recursive --nosave {{nazwa_pakietu}}`

- Usuń pakiet bez pytania:

`sudo pacman --remove --noconfirm {{nazwa_pakietu}}`

- Usuń pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Usuń pakiet i wszystke pakiety, które od niego zależą:

`sudo pacman --remove --cascade {{nazwa_pakietu}}`

- Wyświetl pakiety, na które wpływ miałaby komenda (nie usuwa żadnych pakietów):

`pacman --remove --print {{nazwa_pakietu}}`

- Wyświetl pomoc dla tej komendy:

`pacman --remove --help`
