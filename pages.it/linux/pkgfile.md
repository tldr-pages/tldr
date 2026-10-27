# pkgfile

> Cerca file da pacchetti nei repository ufficiali su sistemi basati su Arch.
> Vedi anche: `pacman files`.
> Maggiori informazioni: <https://manned.org/pkgfile>.

- Sincronizza il database pkgfile:

`sudo pkgfile --update`

- Cerca un pacchetto che possiede un file specifico:

`pkgfile {{nome_file}}`

- Elenca tutti i file forniti da un pacchetto:

`pkgfile --list {{pacchetto}}`

- Elenca gli eseguibili forniti da un pacchetto:

`pkgfile --list --binaries {{pacchetto}}`

- Cerca un pacchetto che possiede un file specifico usando corrispondenza senza distinzione maiuscole/minuscole:

`pkgfile --ignorecase {{nome_file}}`

- Cerca un pacchetto che possiede un file specifico nelle directory `bin` o `sbin`:

`pkgfile --binaries {{nome_file}}`

- Cerca un pacchetto che possiede un file specifico, mostrando la versione del pacchetto:

`pkgfile --verbose {{nome_file}}`

- Cerca un pacchetto che possiede un file specifico in un repository specifico:

`pkgfile --repo {{nome_repository}} {{nome_file}}`
