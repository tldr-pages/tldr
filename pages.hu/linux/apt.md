# apt

> Csomagkezelő segédprogram Debian alapú disztribúciókhoz. A `apt-get` ajánlott helyettesítője, ha interaktívan használják az Ubuntu 16.04 és újabb verziókban. Más csomagkezelők egyenértékű parancsaiért lásd: https: [//wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Frissíti az elérhető csomagok és verziók listáját (ajánlott más `apt` parancsok előtt futtatni):

`sudo apt update`

- Egy adott csomag keresése:

`apt search {{package}}`

- Egy csomag információinak megjelenítése:

`apt show {{package}}`

- Egy csomag telepítése vagy frissítése a legújabb elérhető verzióra:

`sudo apt install {{package}}`

- Egy csomag eltávolítása (a `purge` parancs használatával a csomag konfigurációs fájljai is eltávolíthatók):

`sudo apt remove {{package}}`

- Az összes telepített csomag frissítése a legújabb elérhető verzióra:

`sudo apt upgrade`

- Az összes csomag listázása:

`apt list`

- Telepített csomagok listázása:

`apt list --installed`
