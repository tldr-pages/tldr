# pacman-key

> Skrypt opakowujący dla GnuPG używany do zarządzania pękiem kluczy pacmana.
> Zobacz także: `pacman`.
> Więcej informacji: <https://manned.org/pacman-key>.

- Zainicjalizuj pęk kluczy pacmana:

`sudo pacman-key --init`

- Dodaj domyślne klucze Arch Linuksa:

`sudo pacman-key --populate`

- Wyświetl klucze z pęku publicznego:

`pacman-key {{[-l|--list-keys]}}`

- Dodaj podane klucze:

`sudo pacman-key {{[-a|--add]}} {{ścieżka/do/klucza.gpg}}`

- Pobierz klucz z serwera kluczy:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|imię|email}}"`

- Wyświetl odcisk podanego klucza:

`pacman-key {{[-f|--finger]}} "{{uid|imię|email}}"`

- Podpisz zaimportowany klucz lokalnie:

`sudo pacman-key --lsign-key "{{uid|imię|email}}"`

- Usuń podany klucz:

`sudo pacman-key {{[-d|--delete]}} "{{uid|imię|email}}"`
