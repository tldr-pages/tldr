# pacstrap

> Arch Linux script de instalare pentru a instala pachete în directorul rădăcină nou specificat.
> Mai multe informaţii: <https://man.archlinux.org/man/pacstrap.8>

- Instalați pachetul `base`, kernel-ul Linux și firmware-ul pentru hardware-ul comun:

`pacstrap {{path/to/new/root}} {{base}} {{linux}} {{linux-firmware}}`

- Instalați pachetul `base`, kernelul Linux LTS și instrumentele de construire de bază:

`pacstrap {{path/to/new/root}} {{base}} {{base-devel}} {{linux-lts}}`

- Instalați pachetele fără a copia lista de oglinzi a gazdei la țintă:

`pacstrap -M {{path/to/new/root}} {{packages}}`

- Utilizați un fișier de configurare alternativ pentru Pacman:

`pacstrap -C {{path/to/pacman.conf}} {{path/to/new/root}} {{packages}}`

- Instalați pachetele utilizând cache-ul pachetului pe gazdă în loc de pe țintă:

`pacstrap -c {{path/to/new/root}} {{packages}}`

- Instalați pachetele fără a copia brelocul Pacman al gazdei la țintă:

`pacstrap -G {{path/to/new/root}} {{packages}}`

- Instalați pachetele în modul interactiv (solicitări de confirmare):

`pacstrap -i {{path/to/new/root}} {{packages}}`

- Instalați pachete utilizând fișiere pachet:

`pacstrap -U {{path/to/new/root}} {{path/to/package1}} {{path/to/package2}}`
