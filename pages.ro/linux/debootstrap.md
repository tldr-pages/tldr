# debootstrap

> Creează un sistem Debian de bază.
> Mai multe informaţii: <https://wiki.debian.org/Debootstrap>

- Creați un sistem de lansare stabil Debian în directorul `debian-root`:

`sudo debootstrap stable {{path/to/debian-root/}} http://deb.debian.org/debian`

- Creați un sistem Ubuntu 20.04 în interiorul directorului `focal-rădăcină” cu o oglindă locală:

`sudo debootstrap focal {{path/to/focal-root/}} {{file:///path/to/mirror/}}`

- Comutați la un sistem bootstrapped:

`sudo chroot {{path/to/root}}`

- Lista de versiuni disponibile:

`ls /usr/share/debootstrap/scripts/`
