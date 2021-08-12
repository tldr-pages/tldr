# makepkg

> Creează un pachet care poate fi instalat cu managerul de pachete `pacman`.
> Execută comenzile dintr-un fișier `PKGBUILD `pentru a construi pachetul.
> Mai multe informaţii: <https://wiki.archlinux.org/index.php/Makepkg>

- Efectuați un pachet (rulați în același director ca un „PKGBUILD”):

`makepkg`

- Efectuați un pachet și instalați dependențele sale:

`makepkg --syncdeps`

- La fel ca mai sus, dar instalați pachetul cu `pacman' când ați terminat:

`makepkg --syncdeps --install`

- Faceți un pachet, dar ignorați sumele de control ale sursei:

`makepkg --skipchecksums`
