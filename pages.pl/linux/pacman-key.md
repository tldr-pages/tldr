# pacman-key

> Skrypt opakowujący dla GnuPG używany do zarządzania pękiem kluczy pacmana.
> Zobacz także: `pacman`.
> Więcej informacji: <https://man.archlinux.org/man/pacman-key>.

- Zainicjalizuj pęk kluczy pacmana:

`sudo pacman-key --init`

- Dodaj domyślne klucze Arch Linuksa:

`sudo pacman-key --populate {{archlinux}}`

- Wyświetl klucze z pęku publicznego:

`pacman-key --list-keys`

- Dodaj podane klucze:

`sudo pacman-key --add {{ścieżka/do/klucza.gpg}}`

- Pobierz klucz z serwera kluczy:

`sudo pacman-key --recv-keys "{{uid|imię|email}}"`

- Wyświetl odcisk podanego klucza:

`pacman-key --finger "{{uid|imię|email}}"`

- Podpisz zaimportowany klucz lokalnie:

`sudo pacman-key --lsign-key "{{uid|imię|email}}"`

- Usuń podany klucz:

`sudo pacman-key --delete "{{uid|imię|email}}"`
