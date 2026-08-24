# pacman --remove

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`.
> Więcej informacji: <https://manned.org/pacman.8>.

- Usuń pakiet i jego zależności:

`sudo pacman -Rs {{nazwa_pakietu}}`

- Usuń pakiet, jego zależności i pliki konfiguracyjne:

`sudo pacman -Rsn {{nazwa_pakietu}}`

- Usuń pakiet bez pytania:

`sudo pacman -R --noconfirm {{nazwa_pakietu}}`

- Usuń pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Usuń pakiet i wszystke pakiety, które od niego zależą:

`sudo pacman -Rc {{nazwa_pakietu}}`

- Wyświetl pakiety, na które wpływ miałaby komenda (nie usuwa żadnych pakietów):

`pacman -Rp {{nazwa_pakietu}}`

- Wyświetl pomoc dla tej komendy:

`pacman -Rh`
