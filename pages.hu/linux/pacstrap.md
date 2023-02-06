# pacstrap

> Arch Linux telepítő szkript a csomagok telepítéséhez a megadott új gyökérkönyvtárba. További információ: <https://man.archlinux.org/man/pacstrap.8>.

- Telepítse a `base` csomagot, a Linux kernelt és a firmware-t az általános hardverekhez:

`pacstrap {{path/to/new/root}} {{base}} {{linux}} {{linux-firmware}}`

- Telepítse a `base` csomagot, a Linux LTS kernelt és a `base-devel` építőeszközöket:

`pacstrap {{path/to/new/root}} {{base}} {{base-devel}} {{linux-lts}}`

- Telepítse a csomagokat anélkül, hogy a hoszt tükörlistáját átmásolná a célpontra:

`pacstrap -M {{path/to/new/root}} {{packages}}`

- Alternatív konfigurációs fájl használata a Pacman számára:

`pacstrap -C {{path/to/pacman.conf}} {{path/to/new/root}} {{packages}}`

- Telepítse a csomagokat a csomagtár használatával a gazdán, ahelyett, hogy a célpontra telepítené:

`pacstrap -c {{path/to/new/root}} {{packages}}`

- Csomagok telepítése a hoszt pacman kulcstárának a célpontra való másolása nélkül:

`pacstrap -G {{path/to/new/root}} {{packages}}`

- Csomagok telepítése interaktív módban (megerősítést kér):

`pacstrap -i {{path/to/new/root}} {{packages}}`

- Csomagok telepítése csomagfájlok használatával:

`pacstrap -U {{path/to/new/root}} {{path/to/package1}} {{path/to/package2}}`
