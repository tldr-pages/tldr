# pacman --upgrade

> Arch Linux pakketbeheer hulpprogramma.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman.8>.

- Installeer een of meerdere pakketten vanuit bestanden:

`sudo pacman -U {{pad/naar/pakket1.pkg.tar.zst pad/naar/pakket2.pkg.tar.zst ...}}`

- Installeer een pakket zonder vragen te stellen:

`sudo pacman -U --noconfirm {{pad/naar/pakket.pkg.tar.zst}}`

- Overschrijf conflicterende bestanden tijdens het installeren van een pakket:

`sudo pacman -U --overwrite {{pad/naar/bestand}} {{pad/naar/pakket.pkg.tar.zst}}`

- Installeer een pakket en sla de controles van afhankelijkhei[d]sversie over:

`sudo pacman -Ud {{pad/naar/pakket.pkg.tar.zst}}`

- Haal pakketten op en toon ([p]) welke beïnvloed worden door een upgrade (installeert geen pakketten):

`pacman -Up {{pad/naar/pakket.pkg.tar.zst}}`

- Toon de [h]elp:

`pacman -Uh`
