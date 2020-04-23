# deluge

> Client BItTorrent da linea di comando.
> Maggiori informazioni: <https://deluge-torrent.org>.

- Scarica un torrent:

`deluge {{url|magnet|percorso/a/file}}`

- Scarica un torrent utilizzando uno specifico file di configurazione:

`deluge -c {{percorso/a/file_configurazione}} {{url|magnet|percorso/a/file}}`

- Scarica un torrent ed avvia una specifica interfaccia utente:

`deluge -u {{gtk|web|console}} {{url|magnet|percorso/a/file}}`

- Scarica un torrent e scrivi il log in un file:

`deluge -l {{percorso/a/file_log}} {{url|magnet|percorso/a/file}}`
