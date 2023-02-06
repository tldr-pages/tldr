# debootstrap

> Alap Debian rendszer létrehozása. További információ: <https://wiki.debian.org/Debootstrap>.

- Hozzon létre egy Debian stabil kiadású rendszert a `debian-root` könyvtárban:

`sudo debootstrap stable {{path/to/debian-root/}} http://deb.debian.org/debian`

- Hozzon létre egy minimális rendszert, amely csak a szükséges csomagokat tartalmazza:

`sudo debootstrap --variant=minbase stable {{path/to/debian-root/}}`

- Hozzon létre egy Ubuntu 20.04 rendszert a `focal-root` könyvtáron belül egy helyi tükörrel:

`sudo debootstrap focal {{path/to/focal-root/}} {{file:///path/to/mirror/}}`

- Váltson bootstrapped rendszerre:

`sudo chroot {{path/to/root}}`

- Az elérhető kiadások listázása:

`ls /usr/share/debootstrap/scripts/`
