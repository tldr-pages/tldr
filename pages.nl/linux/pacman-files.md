# pacman --files

> Raadpleeg de lokale bestandendatabase.
> Zie ook: `pkgfile`.
> Meer informatie: <https://manned.org/pacman.8>.

- Werk de pakketdatabase bij:

`sudo pacman -Fy`

- Zoek het pakket dat een specifiek bestand ([F]) bezit:

`pacman -F {{bestandsnaam}}`

- Zoek het pakket dat een specifiek bestand ([F]) bezit, met behulp van een `rege[x]`:

`pacman -Fx '{{regex}}'`

- Maak een lijst van alleen de pakketnamen:

`pacman -Fq {{bestandsnaam}}`

- Toon ([l]) de bestanden ([F]) die eigendom zijn van een specifiek pakket:

`pacman -Fl {{pakket}}`

- Toon de [h]elp:

`pacman -Fh`
