# emerge

> Gentoo Linux csomagkezelő segédprogram. Más csomagkezelőkben használt, ezzel egyenértékű parancsokért lásd: https: [//wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://wiki.gentoo.org/wiki/Portage#emerge>.

- Az összes csomag szinkronizálása:

`emerge --sync`

- Az összes csomag frissítése, beleértve a függőségeket is:

`emerge -uDNav @world`

- Folytassa a sikertelen frissítést, kihagyva a hibás csomagot:

`emerge --resume --skipfirst`

- Új csomag telepítése, megerősítéssel:

`emerge -av {{package_name}}`

- Csomag eltávolítása, megerősítéssel:

`emerge -Cav {{package_name}}`

- Elárvult (csak függőségként telepített) csomagok eltávolítása:

`emerge -avc`

- Keresés a csomagadatbázisban egy kulcsszóra:

`emerge -S {{keyword}}`
