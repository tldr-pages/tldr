# deluge

> Un client BitTorrent linie de comandă.
> Mai multe informaţii: <https://deluge-torrent.org>

- Descarcă un torent:

`deluge {{url|magnet|path/to/file}}`

- Descărcați un torrent utilizând un fișier de configurare specific:

`deluge -c {{path/to/configuration_file}} {{url|magnet|path/to/file}}`

- Descărcați un torent și lansați interfața cu utilizatorul specificată:

`deluge -u {{gtk|web|console}} {{url|magnet|path/to/file}}`

- Descărcați un torent și ieșiți jurnalul într-un fișier:

`deluge -l {{path/to/log_file}} {{url|magnet|path/to/file}}`
