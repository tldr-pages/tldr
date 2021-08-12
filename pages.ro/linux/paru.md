# paru

> Un ajutor AUR și ambalaj pacman.
> Mai multe informaţii: <https://github.com/Morganamilo/paru>

- Căutarea și instalarea interactivă a unui pachet:

`paru {{package_name_or_seach_term}}`

- Sincronizați și actualizați toate pachetele:

`paru`

- Upgrade pachete AUR:

`paru -Sua`

- Obțineți informații despre un pachet:

`paru -Si {{package_name}}`

- Descărcați `PKGBUILD `și alte fișiere sursă de pachete de la AUR sau ABS:

`paru --getpkgbuild {{package_name}}`

- Afișează fișierul `PKGBUILD `al unui pachet:

`paru --getpkgbuild --print {{package_name}}`
