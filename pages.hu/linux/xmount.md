# xmount

> Gyorsan konvertál több bemeneti és kimeneti merevlemezkép-típus között, opcionális írási gyorsítótár támogatással.
> Virtuális fájlrendszert hoz létre a FUSE (Filesystem in Userspace) segítségével, amely a bemeneti kép virtuális reprezentációját tartalmazza.
> További információ: <https://manned.org/xmount>.

- A `.raw` képfájlt egy DMG konténerfájlba mountolja:

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{mountpoint}}`

- Az írási gyorsítótár támogatással rendelkező EWF-képfájlt egy VHD-fájlba szereli, amelyből bootolni lehet:

`xmount --cache {{path/to/cache.ovl}} --in {{ewf}} {{path/to/image.E??}} --out {{vhd}} {{mountpoint}}`

- Az első partíció 2048-as szektorba történő mountolása egy új `.raw` képfájlba:

`xmount --offset {{2048}} --in {{raw}} {{path/to/image.dd}} --out {{raw}} {{mountpoint}}`
