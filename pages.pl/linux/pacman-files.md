# pacman --files

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`, `pkgfile`.
> Więcej informacji: <https://manned.org/pacman.8>.

- Zaktualizuj bazę danych pakietów:

`sudo pacman -Fy`

- Znajdź pakiet, do którego należy podany plik:

`pacman -F {{nazwa_pliku}}`

- Znajdź pakiet, do którego należy podany plik, używając wyrażenia regularnego:

`pacman -Fx '{{wyrażenie_regularne}}'`

- Wyświetl tylko nazwy pakietów:

`pacman -Fq {{nazwa_pliku}}`

- Wyświetl pliki należące do podanego pakietu:

`pacman -Fl {{nazwa_pakietu}}`

- Wyświetl pomoc:

`pacman -Fh`
