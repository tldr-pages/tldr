# pacman-key

> Wrapper-script voor GnuPG, gebruikt om de keyring van `pacman` te beheren.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman-key>.

- Initialiseer de keyring van `pacman`:

`sudo pacman-key --init`

- Voeg de standaard Arch Linux-sleutels toe:

`sudo pacman-key --populate`

- Toon sleutels uit de publieke keyring:

`pacman-key {{[-l|--list-keys]}}`

- Voeg de gespecificeerde sleutels toe:

`sudo pacman-key {{[-a|--add]}} {{pad/naar/sleutelbestand.gpg}}`

- Ontvang een sleutel van een keyserver:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|naam|email}}"`

- Toon de vingerafdruk van een specifieke sleutel:

`pacman-key {{[-f|--finger]}} "{{uid|naam|email}}"`

- Onderteken een geïmporteerde sleutel lokaal:

`sudo pacman-key --lsign-key "{{uid|naam|email}}"`

- Verwijder een specifieke sleutel:

`sudo pacman-key {{[-d|--delete]}} "{{uid|naam|email}}"`
