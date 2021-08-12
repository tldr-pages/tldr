# quilt

> Instrument pentru gestionarea unei serii de patch-uri.
> Mai multe informaţii: <https://savannah.nongnu.org/projects/quilt>

- Importați o corecție existentă dintr-un fișier:

`quilt import {{path/to/filename.patch}}`

- Creează un nou patch:

`quilt new {{filename.patch}}`

- Adăugați un fișier la patch-ul curent:

`quilt add {{path/to/file}}`

- După editarea fișierului, reîmprospătați patch-ul curent cu modificările:

`quilt refresh`

- Aplicați toate patch-urile din fișierul de serie:

`quilt push -a`

- Eliminaţi toţi plasturii aplicaţi:

`quilt pop -a`
