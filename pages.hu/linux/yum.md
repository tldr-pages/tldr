# yum

> Csomagkezelő segédprogram RHEL, Fedora és CentOS (régebbi verziókhoz). Más csomagkezelők megfelelő parancsaiért lásd: [https://wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://manned.org/yum>.

- Új csomag telepítése:

`yum install {{package}}`

- Telepítsen új csomagot, és feltételezze, hogy minden kérdésre igennel válaszol (a frissítéssel is működik, nagyszerű az automatikus frissítésekhez):

`yum -y install {{package}}`

- Keresse meg azt a csomagot, amely egy adott parancsot biztosít:

`yum provides {{command}}`

- Egy csomag eltávolítása:

`yum remove {{package}}`

- A telepített csomagok elérhető frissítéseinek megjelenítése:

`yum check-update`

- A telepített csomagok frissítése a legújabb elérhető verziókra:

`yum upgrade`
