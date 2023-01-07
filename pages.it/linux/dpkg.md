# dpkg

> Gestore di pacchetti Debian.
> Alcuni comandi aggiuntivi, come `dpkg deb`, hanno la propria documentazione.
> Maggiori informazioni: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Installa un pacchetto:

`dpkg -i {{percorso/del/file.deb}}`

- Rimuove un pacchetto:

`dpkg -r {{nome_del_pacchetto}}`

- Elenca i pacchetti installati:

`dpkg -l {{espressione_per_la_ricerca}}`

- Elenca i contenuti di un pacchetto:

`dpkg -L {{nome_del_pacchetto}}`

- Elenca i contenuti di un file pacchetto locale:

`dpkg -c {{percorso/del/file.deb}}`

- Trova a quale pacchetto appartiene un file:

`dpkg -S {{filename}}`
