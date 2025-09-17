# pacman --database

> Werk op de database van het Arch Linux pakket.
> Wijzig bepaalde attributen van de geïnstalleerde pakketten.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman.8>.

- Markeer een pakket als impliciet geïnstalleerd:

`sudo pacman -D --asdeps {{pakket}}`

- Markeer een pakket als expliciet geïnstalleerd:

`sudo pacman -D --asexplicit {{pakket}}`

- Chec[k] dat alle pakket-afhankelijkheden zijn geïnstalleerd:

`pacman -Dk`

- Chec[k] de sync [D]atabase om ervoor te zorgen dat alle gespecificeerde afhankelijkheden van downloadbare pakketten beschikbaar zijn:

`pacman -Dkk`

- Chec[k] en toon in stille ([q]) modus (alleen foutmeldingen worden weergegeven):

`pacman -Dkq`

- Toon de [h]elp:

`pacman -Dh`
