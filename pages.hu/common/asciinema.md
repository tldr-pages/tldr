# asciinema

> Felveheti és visszajátszhatja a terminál üléseket, és opcionálisan megoszthatja azokat az asciinema.org oldalon. További információ: <https://asciinema.org/docs/usage>.

- Kapcsolja a `asciinema` helyi telepítését egy asciinema.org fiókhoz:

`asciinema auth`

- Készítsen új felvételt (ha elkészült, a felhasználónak fel kell töltenie vagy helyben el kell mentenie):

`asciinema rec`

- Készítsen új felvételt és mentse el egy helyi fájlba:

`asciinema rec {{path/to/file}}.cast`

- Egy terminálfelvétel lejátszása egy helyi fájlból:

`asciinema play {{path/to/file}}.cast`

- Az asciinema.org-on tárolt terminálfelvétel újrajátszása:

`asciinema play https://asciinema.org/a/{{cast_id}}`

- Új felvétel készítése, az üresjárati időt legfeljebb 2,5 másodpercre korlátozva:

`asciinema rec -i {{2.5}}`

- Egy helyileg mentett felvétel teljes kimenete kinyomtatása:

`asciinema cat {{path/to/file}}.cast`

- Helyileg mentett terminálos munkamenet feltöltése az asciinema.org-ra:

`asciinema upload {{path/to/file}}.cast`
