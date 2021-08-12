# pkgfile

> Instrument pentru căutarea fișierelor din pachetele din depozitele oficiale ale sistemelor bazate pe arc.
> A se vedea, de asemenea, `Pacman fisiere ', descriind utilizarea `pacman —fisiere'.
> Mai multe informaţii: <https://man.archlinux.org/man/extra/pkgfile/pkgfile.1>

- Sincronizați baza de date pkgfile:

`sudo pkgfile --update`

- Căutați un pachet care deține un anumit fișier:

`pkgfile {{filename}}`

- Listează toate fișierele furnizate de un pachet:

`pkgfile --list {{package_name}}`

- Listează numai fișierele furnizate de un pachet situat în directorul `bin` sau `sbin`:

`pkgfile --list --binaries {{package_name}}`

- Cauta un pachet care detine un anumit fisier folosind potrivire insensibila la litere:

`pkgfile --ignorecase {{filename}}`

- Căutați un pachet care deține un anumit fișier în directorul `bin` sau `sbin`:

`pkgfile --binaries {{filename}}`

- Căutați un pachet care deține un anumit fișier, afișând versiunea pachetului:

`pkgfile --verbose {{filename}}`

- Căutați un pachet care deține un anumit fișier într-un anumit depozit:

`pkgfile --repo {{repository_name}} {{filename}}`
