# dnf

> Csomagkezelő segédprogram RHEL, Fedora és CentOS rendszerekhez (helyettesíti a yum-ot). Más csomagkezelők megfelelő parancsaiért lásd: [https://wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://dnf.readthedocs.io>.

- A telepített csomagok frissítése a legújabb elérhető verziókra:

`sudo dnf upgrade`

- Csomagok keresése kulcsszavak segítségével:

`dnf search {{keywords}}`

- Részletek megjelenítése egy csomagról:

`dnf info {{package}}`

- Új csomag telepítése (a `-y` használatával minden kérést automatikusan megerősíthet):

`sudo dnf install {{package}}`

- Csomag eltávolítása:

`sudo dnf remove {{package}}`

- Telepített csomagok listázása:

`dnf list --installed`

- Megtalálni, hogy mely csomagok nyújtanak egy adott fájlt:

`dnf provides {{file}}`

- Az összes korábbi művelet megtekintése:

`dnf history`
