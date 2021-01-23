# dpkg

> Gestore di pacchetti Debian.
> Maggiori informazioni: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>.

- Installa un pacchetto:

`dpkg -i {{percorso/al/file.deb}}`

- Rimuove un pacchetto:

`dpkg -r {{nome_del_pacchetto}}`

- Elenca i pacchetti installati:

`dpkg -l {{espressione_per_la_ricerca}}`

- Elenca i contenuti di un pacchetto:

`dpkg -L {{nome_del_pacchetto}}`

- Elenca i contenuti di un file pacchetto locale:

`dpkg -c {{percorso/al/file.deb}}`

- Trova a quale pacchetto appartiene un file:

`dpkg -S {{filename}}`
