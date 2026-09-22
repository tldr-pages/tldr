# pkgfile

> Zoek bestanden van pakketten in de officiële repositories op Arch-gebaseerde systemen.
> Zie ook: `pacman --files`.
> Meer informatie: <https://manned.org/pkgfile>.

- Synchroniseer de pkgfile-database:

`sudo pkgfile --update`

- Zoek naar een pakket dat een specifiek bestand bezit:

`pkgfile {{bestandsnaam}}`

- Toon alle bestanden die door een pakket worden geleverd:

`pkgfile --list {{pakket}}`

- Toon uitvoerbare bestanden die door een pakket worden geleverd:

`pkgfile --list --binaries {{pakket}}`

- Zoek naar een pakket dat een specifiek bestand bezit, met hoofdletterongevoelige matching:

`pkgfile --ignorecase {{bestandsnaam}}`

- Zoek naar een pakket dat een specifiek bestand bezit in de map `bin` of `sbin`:

`pkgfile --binaries {{bestandsnaam}}`

- Zoek naar een pakket dat een specifiek bestand bezit, met weergave van de pakketversie:

`pkgfile --verbose {{bestandsnaam}}`

- Zoek naar een pakket dat een specifiek bestand bezit in een specifieke repository:

`pkgfile --repo {{repository_naam}} {{bestandsnaam}}`
