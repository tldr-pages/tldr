# pacman --files

> Arch Linux pakketbeheer hulpprogramma.
> Zie ook: `pacman`,` pkgfile`.
> Meer informatie: <https://manned.org/pacman.8>.

- Werk de pakketdatabase bij:

`sudo pacman -Fy`

- Zoek het pakket dat een specifiek bestand ([F]) bezit:

`pacman -F {{bestandsnaam}}`

- Zoek het pakket dat een specifiek bestand ([F]) bezit, met behulp van een reguliere e[x]pressie:

`pacman -Fx '{{reguliere_expressie}}'`

- Maak een lijst van alleen de pakketnamen:

`pacman -Fq {{bestandsnaam}}`

- Toon ([l]) de bestanden ([F]) die eigendom zijn van een specifiek pakket:

`pacman -Fl {{pakket}}`

- Toon de [h]elp:

`pacman -Fh`
