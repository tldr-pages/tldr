# pacman --files

> Narzędzie do zarządzania pakietami w Arch Linuksie.
> Zobacz także: `pacman`, `pkgfile`.
> Więcej informacji: <https://man.archlinux.org/man/pacman.8>.

- Zaktualizuj bazę danych pakietów:

`sudo pacman --files --refresh`

- Znajdź pakiet, do którego należy podany plik:

`pacman --files {{nazwa_pliku}}`

- Znajdź pakiet, do którego należy podany plik, używając wyrażenia regularnego:

`pacman --files --regex '{{wyrażenie_regularne}}'`

- Wyświetl tylko nazwy pakietów:

`pacman --files --quiet {{nazwa_pliku}}`

- Wyświetl pliki należące do podanego pakietu:

`pacman --files --list {{nazwa_pakietu}}`

- Wyświetl pomoc:

`pacman --files --help`
