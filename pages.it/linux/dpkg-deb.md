# dpkg-deb

> Impacchetta, spacchetta e fornisce informazioni su archivi Debian.
> Maggiori informazioni: <https://manpages.debian.org/latest/dpkg/dpkg-deb.html>.

- Mostra le informazioni riguardo ad un pacchetto:

`dpkg-deb --info {{percorso/del/file.deb}}`

- Mostra il nome e la versione del pacchetto in una singola riga:

`dpkg-deb --show {{percorso/del/file.deb}}`

- Elenca i contenuti del pacchetto:

`dpkg-deb --contents {{percorso/del/file.deb}}`

- Estrae i contenuti del pacchetto in una cartella:

`dpkg-deb --extract {{percorso/del/file.deb}} {{percorso/della/cartella}}`

- Crea una pacchetto a partire da una cartella specificata:

`dpkg-deb --build {{percorso/della/cartella}}`
