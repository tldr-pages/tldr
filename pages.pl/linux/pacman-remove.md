# pacman --remove

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Więcej informacji: <https://manned.org/pacman.8>.

- Usuń pakiet i jego zależności:

`sudo pacman -Rs {{pakiet}}`

- Usuń pakiet, jego zależności i pliki konfiguracyjne:

`sudo pacman -Rsn {{pakiet}}`

- Usuń pakiet bez pytania:

`sudo pacman -R --noconfirm {{pakiet}}`

- Usuń pakiety-sieroty (zainstalowane jako zależności ale nie są już wymagane przez żaden pakiet):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Usuń pakiet i wszystke pakiety, które od niego zależą:

`sudo pacman -Rc {{pakiet}}`

- Wyświetl pakiety, na które wpływ miałaby komenda (nie usuwa żadnych pakietów):

`pacman -Rp {{pakiet}}`

- Wyświetl pomoc dla tej komendy:

`pacman -Rh`
