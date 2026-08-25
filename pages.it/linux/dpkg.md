# dpkg

> Gestore di pacchetti Debian.
> Alcuni sottocomandi, come `deb`, hanno la propria documentazione d'uso.
> Per i comandi equivalenti in altri gestori di pacchetti, vedi <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Maggiori informazioni: <https://manned.org/dpkg>.

- Installa un pacchetto:

`sudo dpkg {{[-i|--install]}} {{percorso/del/file.deb}}`

- Rimuove un pacchetto:

`sudo dpkg {{[-r|--remove]}} {{pacchetto}}`

- Elenca i pacchetti installati:

`dpkg {{[-l|--list]}} {{espressione}}`

- Elenca i contenuti di un pacchetto:

`dpkg {{[-L|--listfiles]}} {{pacchetto}}`

- Elenca i contenuti di un file pacchetto locale:

`dpkg {{[-c|--contents]}} {{percorso/del/file.deb}}`

- Trova a quale pacchetto appartiene un file:

`dpkg {{[-S|--search]}} {{percorso/del/file}}`

- Rimuove completamente un pacchetto installato o già rimosso, inclusa la configurazione:

`sudo dpkg {{[-P|--purge]}} {{pacchetto}}`
