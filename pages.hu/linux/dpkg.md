# dpkg

> Debian csomagkezelő.
> Néhány alparancsnak, mint például a `dpkg deb`, saját használati dokumentációja van.
> Más csomagkezelőkben az ezzel egyenértékű parancsokat lásd: https: [//wiki.archlinux.org/title/Pacman/Rosetta](https://wiki.archlinux.org/title/Pacman/Rosetta).
> További információ: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Telepítsen egy csomagot:

`dpkg -i {{path/to/file.deb}}`

- Csomag eltávolítása:

`dpkg -r {{package_name}}`

- Telepített csomagok listázása:

`dpkg -l {{pattern}}`

- Egy csomag tartalmának listázása:

`dpkg -L {{package_name}}`

- Egy helyi csomagfájl tartalmának listázása:

`dpkg -c {{path/to/file.deb}}`

- Megtudni, melyik csomag tulajdonában van egy fájl:

`dpkg -S {{filename}}`
