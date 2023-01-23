# pacman-key

> A GnuPG csomagolószkriptje, amely a pacman kulcstárának kezelésére szolgál. További információ: <https://man.archlinux.org/man/pacman-key>.

- A pacman kulcskarika inicializálása:

`sudo pacman-key --init`

- Adja hozzá az alapértelmezett Arch Linux kulcsokat:

`sudo pacman-key --populate {{archlinux}}`

- A nyilvános kulcsok listázása a nyilvános kulcsgyűjteményből:

`pacman-key --list-keys`

- A megadott kulcsok hozzáadása:

`sudo pacman-key --add {{path/to/keyfile.gpg}}`

- Kulcs fogadása egy kulcskiszolgálótól:

`sudo pacman-key --recv-keys "{{uid|name|email}}"`

- Egy adott kulcs ujjlenyomatának kinyomtatása:

`pacman-key --finger "{{uid|name|email}}"`

- Importált kulcs helyi aláírása:

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- Egy adott kulcs eltávolítása:

`sudo pacman-key --delete "{{uid|name|email}}"`
