# dpkg-deb

> Impacchetta, spacchetta e fornisce informazioni su archivi Debian.
> Maggiori informazioni: <https://manpages.debian.org/latest/dpkg/dpkg-deb.html>.

- Mostra le informazioni riguardo ad un pacchetto:

`dpkg-deb --info {{percorso/al/file.deb}}`

- Mostra il nome e la versione del pacchetto in una singola riga:

`dpkg-deb --show {{percorso/al/file.deb}}`

- Elenca i contenuti del pacchetto:

`dpkg-deb --contents {{percorso/al/file.deb}}`

- Estrae i contenuti del pacchetto in una cartella:

`dpkg-deb --extract {{percorso/al/file.deb}} {{percorso/alla/cartella}}`

- Crea una pacchetto a partire da una cartella specificata:

`dpkg-deb --build {{percorso/alla/cartella}}`
